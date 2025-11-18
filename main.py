"""
Library Management System - Main Application
Integrated GUI with Database and API Integration
"""
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, simpledialog
from PIL import Image, ImageTk
import requests
from io import BytesIO
from datetime import datetime, timedelta
import threading

from db_manager import DatabaseManager
from book_api import BookAPI
from notifications import NotificationManager


class LibraryManagementSystem(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("📚 Library Management System")
        self.geometry("1200x900")
        self.config(bg="#f5f5f5")

        # Initialize modules
        self.db = DatabaseManager()
        self.book_api = BookAPI()
        self.notifications = NotificationManager()

        # Create notebook for tabs
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Create tabs
        self.create_dashboard_tab()
        self.create_book_management_tab()
        self.create_member_management_tab()
        self.create_transaction_tab()
        self.create_reviews_tab()

        # Refresh dashboard on startup
        self.refresh_dashboard()

    # ========== DASHBOARD TAB ==========
    def create_dashboard_tab(self):
        dashboard_frame = ttk.Frame(self.notebook)
        self.notebook.add(dashboard_frame, text="📊 Dashboard")

        # Title
        title_label = tk.Label(
            dashboard_frame,
            text="Library Management Dashboard",
            font=("Arial", 24, "bold"),
            bg="#283593",
            fg="white"
        )
        title_label.pack(fill="x", pady=(0, 20))

        # Statistics Frame
        stats_frame = tk.LabelFrame(
            dashboard_frame,
            text="Key Statistics",
            font=("Arial", 14, "bold"),
            padx=20,
            pady=15,
            bg="#e8eaf6"
        )
        stats_frame.pack(fill="x", padx=20, pady=10)

        self.stats_label = tk.Label(
            stats_frame,
            text="Loading statistics...",
            font=("Arial", 12),
            justify="left",
            bg="#e8eaf6"
        )
        self.stats_label.pack(anchor="w", padx=10)

        # Quick Actions
        actions_frame = tk.LabelFrame(
            dashboard_frame,
            text="Quick Actions",
            font=("Arial", 14, "bold"),
            padx=20,
            pady=15,
            bg="#e8eaf6"
        )
        actions_frame.pack(fill="x", padx=20, pady=10)

        btn_frame = tk.Frame(actions_frame, bg="#e8eaf6")
        btn_frame.pack()
        ttk.Button(btn_frame, text="Add Book", command=self.open_add_book_window).grid(row=0, column=0, padx=10, pady=5)
        ttk.Button(btn_frame, text="Issue Book", command=self.open_issue_book_window).grid(row=0, column=1, padx=10, pady=5)
        ttk.Button(btn_frame, text="Register Member", command=self.open_register_member_window).grid(row=0, column=2, padx=10, pady=5)
        ttk.Button(btn_frame, text="Refresh", command=self.refresh_dashboard).grid(row=0, column=3, padx=10, pady=5)

        # Recent Transactions
        recent_frame = tk.LabelFrame(
            dashboard_frame,
            text="Recent Transactions",
            font=("Arial", 14, "bold"),
            padx=20,
            pady=15,
            bg="#e8eaf6"
        )
        recent_frame.pack(fill="both", expand=True, padx=20, pady=10)

        columns = ("date", "member", "book", "status")
        self.recent_tree = ttk.Treeview(recent_frame, columns=columns, show="headings", height=8)
        for col in columns:
            self.recent_tree.heading(col, text=col.replace("_", " ").title())
            self.recent_tree.column(col, width=200)
        self.recent_tree.pack(fill="both", expand=True)

        # Popular Books
        popular_frame = tk.LabelFrame(
            dashboard_frame,
            text="Popular Books",
            font=("Arial", 14, "bold"),
            padx=20,
            pady=15,
            bg="#e8eaf6"
        )
        popular_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.popular_list = tk.Listbox(popular_frame, height=6, font=("Arial", 11))
        self.popular_list.pack(fill="both", expand=True)

    def refresh_dashboard(self):
        """Refresh dashboard statistics and data"""
        stats = self.db.get_statistics()
        stats_text = f"""
📚 Total Books: {stats['total_books']}
👥 Total Members: {stats['total_members']}
📖 Books Issued: {stats['books_issued']}
✅ Available Books: {stats['available_books']}
⚠️ Overdue Books: {stats['overdue_books']}
        """.strip()
        self.stats_label.config(text=stats_text)

        # Refresh recent transactions
        for item in self.recent_tree.get_children():
            self.recent_tree.delete(item)
        
        recent = self.db.get_recent_transactions(limit=10)
        for txn in recent:
            self.recent_tree.insert("", "end", values=(
                txn.get('issue_date', ''),
                txn.get('member_name', ''),
                txn.get('book_title', ''),
                txn.get('status', '')
            ))

        # Refresh popular books
        self.popular_list.delete(0, tk.END)
        popular = self.db.get_popular_books(limit=10)
        for book in popular:
            self.popular_list.insert(tk.END, f"{book['title']} by {book['author']}")

    # ========== BOOK MANAGEMENT TAB ==========
    def create_book_management_tab(self):
        book_frame = ttk.Frame(self.notebook)
        self.notebook.add(book_frame, text="📚 Book Management")

        # Top buttons
        btn_frame = tk.Frame(book_frame, bg="#e3f2fd")
        btn_frame.pack(fill="x", padx=20, pady=10)
        ttk.Button(btn_frame, text="Add New Book (ISBN Lookup)", command=self.open_add_book_window).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Search Books", command=self.open_search_books_window).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Update Book", command=self.open_update_book_window).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="View Details", command=self.view_selected_book).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Export to CSV", command=self.export_books_csv).pack(side="left", padx=5)

        # Books table
        table_frame = tk.Frame(book_frame)
        table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        columns = ("id", "isbn", "title", "author", "available", "total")
        self.books_tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.books_tree.yview)
        self.books_tree.configure(yscrollcommand=scrollbar.set)

        for col in columns:
            self.books_tree.heading(col, text=col.replace("_", " ").title())
            self.books_tree.column(col, width=150)

        self.books_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.books_tree.bind("<Double-1>", self.on_book_select)

        self.refresh_books_table()

    def refresh_books_table(self):
        """Refresh books table"""
        for item in self.books_tree.get_children():
            self.books_tree.delete(item)
        
        books = self.db.get_all_books()
        for book in books:
            self.books_tree.insert("", "end", values=(
                book['book_id'],
                book.get('isbn', ''),
                book['title'],
                book['author'],
                book['available_copies'],
                book['total_copies']
            ), tags=(book['book_id'],))

    def open_add_book_window(self):
        """Open window to add new book with ISBN lookup"""
        win = tk.Toplevel(self)
        win.title("Add New Book")
        win.geometry("700x600")
        win.config(bg="white")

        # ISBN lookup section
        lookup_frame = tk.LabelFrame(win, text="ISBN Lookup", font=("Arial", 12, "bold"), padx=10, pady=10)
        lookup_frame.pack(fill="x", padx=20, pady=10)

        tk.Label(lookup_frame, text="Enter ISBN:", font=("Arial", 10)).pack(side="left", padx=5)
        isbn_entry = tk.Entry(lookup_frame, width=20, font=("Arial", 10))
        isbn_entry.pack(side="left", padx=5)

        status_label = tk.Label(lookup_frame, text="", fg="blue", font=("Arial", 9))
        status_label.pack(side="left", padx=10)

        def lookup_isbn():
            isbn = isbn_entry.get().strip()
            if not isbn:
                messagebox.showerror("Error", "Please enter an ISBN")
                return
            
            status_label.config(text="Searching...", fg="blue")
            win.update()

            # Fetch book data in a separate thread
            def fetch_book():
                book_data = self.book_api.fetch_book_data(isbn)
                win.after(0, lambda: populate_fields(book_data))

            threading.Thread(target=fetch_book, daemon=True).start()

        def populate_fields(book_data):
            if book_data:
                status_label.config(text="Found!", fg="green")
                title_entry.delete(0, tk.END)
                title_entry.insert(0, book_data.get('title', ''))
                author_entry.delete(0, tk.END)
                author_entry.insert(0, book_data.get('author', ''))
                publisher_entry.delete(0, tk.END)
                publisher_entry.insert(0, book_data.get('publisher', ''))
                year_entry.delete(0, tk.END)
                year_entry.insert(0, str(book_data.get('publication_year', '')))
                category_entry.delete(0, tk.END)
                category_entry.insert(0, book_data.get('category', ''))
                description_text.delete("1.0", tk.END)
                description_text.insert("1.0", book_data.get('description', ''))
                page_count_entry.delete(0, tk.END)
                page_count_entry.insert(0, str(book_data.get('page_count', '')))
                language_entry.delete(0, tk.END)
                language_entry.insert(0, book_data.get('language', ''))
                cover_url_entry.delete(0, tk.END)
                cover_url_entry.insert(0, book_data.get('cover_image_url', ''))

                # Display cover image if available
                if book_data.get('cover_image_url'):
                    display_cover_image(book_data.get('cover_image_url'))
            else:
                status_label.config(text="Not found", fg="red")
                messagebox.showwarning("Not Found", "Book not found. Please enter details manually.")

        ttk.Button(lookup_frame, text="Lookup", command=lookup_isbn).pack(side="left", padx=5)

        # Book details form
        form_frame = tk.LabelFrame(win, text="Book Details", font=("Arial", 12, "bold"), padx=10, pady=10)
        form_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Create scrollable frame
        canvas = tk.Canvas(form_frame, bg="white")
        scrollbar_form = ttk.Scrollbar(form_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="white")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar_form.set)

        # Form fields
        fields = [
            ("ISBN:", "isbn"),
            ("Title:", "title"),
            ("Author:", "author"),
            ("Publisher:", "publisher"),
            ("Publication Year:", "year"),
            ("Category:", "category"),
            ("Page Count:", "page_count"),
            ("Language:", "language"),
            ("Total Copies:", "total_copies"),
            ("Shelf Location:", "shelf_location"),
            ("Cover Image URL:", "cover_url")
        ]

        entries = {}
        row = 0
        for label_text, key in fields:
            tk.Label(scrollable_frame, text=label_text, bg="white", font=("Arial", 10)).grid(row=row, column=0, sticky="w", padx=10, pady=5)
            if key == "description":
                entry = scrolledtext.ScrolledText(scrollable_frame, width=40, height=4, font=("Arial", 9))
                entry.grid(row=row, column=1, padx=10, pady=5)
            else:
                entry = tk.Entry(scrollable_frame, width=40, font=("Arial", 10))
                entry.grid(row=row, column=1, padx=10, pady=5)
            entries[key] = entry
            row += 1

        # Description field
        tk.Label(scrollable_frame, text="Description:", bg="white", font=("Arial", 10)).grid(row=row, column=0, sticky="nw", padx=10, pady=5)
        description_text = scrolledtext.ScrolledText(scrollable_frame, width=40, height=4, font=("Arial", 9))
        description_text.grid(row=row, column=1, padx=10, pady=5)
        entries['description'] = description_text
        row += 1

        # Cover image display
        cover_frame = tk.Frame(scrollable_frame, bg="white")
        cover_frame.grid(row=row, column=0, columnspan=2, pady=10)
        cover_label = tk.Label(cover_frame, text="No cover image", bg="white", width=30, height=10)
        cover_label.pack()

        def display_cover_image(url):
            try:
                response = requests.get(url, timeout=5)
                img = Image.open(BytesIO(response.content))
                img.thumbnail((150, 200))
                photo = ImageTk.PhotoImage(img)
                cover_label.config(image=photo, text="")
                cover_label.image = photo
            except:
                cover_label.config(text="Failed to load image", image="")

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar_form.pack(side="right", fill="y")

        # Get entry references
        isbn_entry_ref = entries.get('isbn', tk.Entry())
        title_entry = entries.get('title', tk.Entry())
        author_entry = entries.get('author', tk.Entry())
        publisher_entry = entries.get('publisher', tk.Entry())
        year_entry = entries.get('year', tk.Entry())
        category_entry = entries.get('category', tk.Entry())
        page_count_entry = entries.get('page_count', tk.Entry())
        language_entry = entries.get('language', tk.Entry())
        total_copies_entry = entries.get('total_copies', tk.Entry())
        shelf_location_entry = entries.get('shelf_location', tk.Entry())
        cover_url_entry = entries.get('cover_url', tk.Entry())

        # Set default values
        total_copies_entry.insert(0, "1")

        def save_book():
            try:
                book_data = {
                    'isbn': isbn_entry_ref.get().strip(),
                    'title': title_entry.get().strip(),
                    'author': author_entry.get().strip(),
                    'publisher': publisher_entry.get().strip(),
                    'publication_year': int(year_entry.get()) if year_entry.get().strip() else None,
                    'category': category_entry.get().strip(),
                    'description': description_text.get("1.0", tk.END).strip(),
                    'cover_image_url': cover_url_entry.get().strip(),
                    'page_count': int(page_count_entry.get()) if page_count_entry.get().strip() else 0,
                    'language': language_entry.get().strip() or 'en',
                    'total_copies': int(total_copies_entry.get()) if total_copies_entry.get().strip() else 1,
                    'shelf_location': shelf_location_entry.get().strip()
                }

                if not book_data['title']:
                    messagebox.showerror("Error", "Title is required")
                    return

                self.db.add_book(book_data)
                messagebox.showinfo("Success", "Book added successfully!")
                self.refresh_books_table()
                self.refresh_dashboard()
                win.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e))
            except Exception as e:
                messagebox.showerror("Error", f"Error adding book: {e}")

        ttk.Button(win, text="Save Book", command=save_book).pack(pady=10)

    def open_search_books_window(self):
        """Open search books window"""
        win = tk.Toplevel(self)
        win.title("Search Books")
        win.geometry("800x500")

        search_frame = tk.Frame(win, padx=20, pady=10)
        search_frame.pack(fill="x")

        tk.Label(search_frame, text="Search:", font=("Arial", 12)).pack(side="left", padx=5)
        search_entry = tk.Entry(search_frame, width=30, font=("Arial", 11))
        search_entry.pack(side="left", padx=5)

        search_by_var = tk.StringVar(value="title")
        search_options = ttk.Combobox(search_frame, textvariable=search_by_var, values=["title", "author", "isbn", "category"], state="readonly", width=15)
        search_options.pack(side="left", padx=5)

        results_tree = ttk.Treeview(win, columns=("id", "isbn", "title", "author", "available"), show="headings", height=15)
        for col in ("id", "isbn", "title", "author", "available"):
            results_tree.heading(col, text=col.title())
            if col == "title":
                results_tree.column(col, width=250)
            else:
                results_tree.column(col, width=120)
        results_tree.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Double-click to view details
        def on_result_select(event):
            selected = results_tree.selection()
            if selected:
                item = results_tree.item(selected[0])
                book_id = item['values'][0]
                win.destroy()
                self.open_book_details_window(book_id)
        
        results_tree.bind("<Double-1>", on_result_select)

        def perform_search():
            search_term = search_entry.get().strip()
            search_by = search_by_var.get()
            
            for item in results_tree.get_children():
                results_tree.delete(item)
            
            if search_term:
                books = self.db.search_books(search_term, search_by)
                if not books:
                    results_tree.insert("", "end", values=("", "", "No results found", "", ""))
                else:
                    for book in books:
                        results_tree.insert("", "end", values=(
                            book['book_id'],
                            book.get('isbn', ''),
                            book['title'],
                            book['author'],
                            f"{book['available_copies']}/{book['total_copies']}"
                        ))
            else:
                # Show all books if no search term
                books = self.db.get_all_books()
                for book in books:
                    results_tree.insert("", "end", values=(
                        book['book_id'],
                        book.get('isbn', ''),
                        book['title'],
                        book['author'],
                        f"{book['available_copies']}/{book['total_copies']}"
                    ))

        ttk.Button(search_frame, text="Search", command=perform_search).pack(side="left", padx=5)
        ttk.Button(search_frame, text="Show All", command=lambda: (search_entry.delete(0, tk.END), perform_search())).pack(side="left", padx=5)
        search_entry.bind("<Return>", lambda e: perform_search())
        
        # Initial load - show all books
        perform_search()

    def open_update_book_window(self):
        """Open update book window"""
        selected = self.books_tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a book to update")
            return
        
        item = self.books_tree.item(selected[0])
        book_id = item['values'][0]
        book = self.db.get_book(book_id)
        
        if not book:
            messagebox.showerror("Error", "Book not found")
            return

        win = tk.Toplevel(self)
        win.title("Update Book")
        win.geometry("500x400")

        # Create form similar to add book but with pre-filled values
        tk.Label(win, text="Update Book Information", font=("Arial", 14, "bold")).pack(pady=10)

        form_frame = tk.Frame(win)
        form_frame.pack(fill="both", expand=True, padx=20, pady=10)

        fields = [
            ("Total Copies:", "total_copies"),
            ("Available Copies:", "available_copies"),
            ("Shelf Location:", "shelf_location")
        ]

        entries = {}
        row = 0
        for label_text, key in fields:
            tk.Label(form_frame, text=label_text).grid(row=row, column=0, sticky="w", pady=5)
            entry = tk.Entry(form_frame, width=30)
            entry.insert(0, str(book.get(key, '')))
            entry.grid(row=row, column=1, pady=5)
            entries[key] = entry
            row += 1

        def update_book():
            try:
                update_data = {
                    'total_copies': int(entries['total_copies'].get()) if entries['total_copies'].get().strip() else book['total_copies'],
                    'available_copies': int(entries['available_copies'].get()) if entries['available_copies'].get().strip() else book['available_copies'],
                    'shelf_location': entries['shelf_location'].get().strip() or book.get('shelf_location', '')
                }
                self.db.update_book(book_id, update_data)
                messagebox.showinfo("Success", "Book updated successfully!")
                self.refresh_books_table()
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Error updating book: {e}")

        ttk.Button(win, text="Update", command=update_book).pack(pady=10)

    def on_book_select(self, event):
        """Handle book selection - double click to view details"""
        selected = self.books_tree.selection()
        if selected:
            item = self.books_tree.item(selected[0])
            book_id = item['values'][0]
            self.open_book_details_window(book_id)
    
    def view_selected_book(self):
        """View details of selected book"""
        selected = self.books_tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a book to view details")
            return
        item = self.books_tree.item(selected[0])
        book_id = item['values'][0]
        self.open_book_details_window(book_id)
    
    def export_books_csv(self):
        """Export books to CSV file"""
        try:
            from tkinter import filedialog
            import csv
            
            filename = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
                title="Export Books to CSV"
            )
            
            if not filename:
                return
            
            books = self.db.get_all_books()
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['book_id', 'isbn', 'title', 'author', 'publisher', 'publication_year', 
                             'category', 'page_count', 'language', 'total_copies', 'available_copies', 'shelf_location']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for book in books:
                    writer.writerow({k: book.get(k, '') for k in fieldnames})
            
            messagebox.showinfo("Success", f"Exported {len(books)} books to {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Error exporting books: {e}")
    
    def open_book_details_window(self, book_id):
        """Open detailed book view window"""
        book = self.db.get_book(book_id)
        if not book:
            messagebox.showerror("Error", "Book not found")
            return
        
        win = tk.Toplevel(self)
        win.title(f"Book Details: {book['title']}")
        win.geometry("700x700")
        win.config(bg="white")
        
        # Main frame with scrollbar
        main_frame = tk.Frame(win, bg="white")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Left side - Cover image
        left_frame = tk.Frame(main_frame, bg="white")
        left_frame.pack(side="left", padx=10)
        
        cover_label = tk.Label(left_frame, text="No cover image", bg="white", width=25, height=35, relief="solid")
        cover_label.pack()
        
        # Load cover image if available
        if book.get('cover_image_url'):
            try:
                response = requests.get(book['cover_image_url'], timeout=5)
                img = Image.open(BytesIO(response.content))
                img.thumbnail((200, 300))
                photo = ImageTk.PhotoImage(img)
                cover_label.config(image=photo, text="")
                cover_label.image = photo
            except:
                cover_label.config(text="Failed to load image")
        
        # Right side - Book details
        right_frame = tk.Frame(main_frame, bg="white")
        right_frame.pack(side="left", fill="both", expand=True, padx=10)
        
        # Title
        tk.Label(right_frame, text=book['title'], font=("Arial", 18, "bold"), bg="white", wraplength=400).pack(anchor="w", pady=(0, 5))
        
        # Author
        tk.Label(right_frame, text=f"By: {book['author']}", font=("Arial", 14), bg="white", fg="#666").pack(anchor="w", pady=(0, 10))
        
        # Details grid
        details_frame = tk.Frame(right_frame, bg="white")
        details_frame.pack(fill="x", pady=10)
        
        details = [
            ("ISBN:", book.get('isbn', 'N/A')),
            ("Publisher:", book.get('publisher', 'N/A')),
            ("Publication Year:", str(book.get('publication_year', 'N/A'))),
            ("Category:", book.get('category', 'N/A')),
            ("Language:", book.get('language', 'N/A')),
            ("Page Count:", str(book.get('page_count', 'N/A'))),
            ("Total Copies:", str(book.get('total_copies', 0))),
            ("Available Copies:", str(book.get('available_copies', 0))),
            ("Shelf Location:", book.get('shelf_location', 'N/A'))
        ]
        
        row = 0
        for label, value in details:
            tk.Label(details_frame, text=label, font=("Arial", 10, "bold"), bg="white").grid(row=row, column=0, sticky="w", pady=3)
            tk.Label(details_frame, text=str(value), font=("Arial", 10), bg="white").grid(row=row, column=1, sticky="w", padx=10, pady=3)
            row += 1
        
        # Description
        tk.Label(right_frame, text="Description:", font=("Arial", 12, "bold"), bg="white").pack(anchor="w", pady=(10, 5))
        desc_text = scrolledtext.ScrolledText(right_frame, width=50, height=8, font=("Arial", 10), wrap=tk.WORD)
        desc_text.insert("1.0", book.get('description', 'No description available'))
        desc_text.config(state="disabled")
        desc_text.pack(fill="both", expand=True, pady=5)
        
        # Reviews section
        reviews_frame = tk.LabelFrame(right_frame, text="Reviews", font=("Arial", 12, "bold"), bg="white")
        reviews_frame.pack(fill="x", pady=10)
        
        reviews = self.db.get_book_reviews(book_id)
        if reviews:
            for review in reviews[:3]:  # Show top 3 reviews
                rating_stars = "⭐" * review['rating'] + "☆" * (5 - review['rating'])
                review_text = f"{review.get('member_name', 'Anonymous')} - {rating_stars}\n{review.get('review_text', '')[:100]}..."
                tk.Label(reviews_frame, text=review_text, font=("Arial", 9), bg="white", wraplength=400, justify="left").pack(anchor="w", padx=10, pady=5)
        else:
            tk.Label(reviews_frame, text="No reviews yet", font=("Arial", 10), bg="white", fg="#999").pack(pady=10)
        
        # Buttons
        btn_frame = tk.Frame(win, bg="white")
        btn_frame.pack(fill="x", padx=20, pady=10)
        ttk.Button(btn_frame, text="Update Book", command=lambda: (win.destroy(), self.open_update_book_window())).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Add Review", command=lambda: (win.destroy(), self.open_add_review_window())).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Close", command=win.destroy).pack(side="right", padx=5)

    # ========== MEMBER MANAGEMENT TAB ==========
    def create_member_management_tab(self):
        member_frame = ttk.Frame(self.notebook)
        self.notebook.add(member_frame, text="👥 Member Management")

        btn_frame = tk.Frame(member_frame, bg="#f3e5f5")
        btn_frame.pack(fill="x", padx=20, pady=10)
        ttk.Button(btn_frame, text="Register New Member", command=self.open_register_member_window).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Update Member", command=self.open_update_member_window).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="View Borrowing History", command=self.open_borrow_history_window).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Send Email Notifications", command=self.open_email_notify_window).pack(side="left", padx=5)

        # Members table
        table_frame = tk.Frame(member_frame)
        table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        columns = ("id", "membership_number", "name", "email", "phone", "status")
        self.members_tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.members_tree.yview)
        self.members_tree.configure(yscrollcommand=scrollbar.set)

        for col in columns:
            self.members_tree.heading(col, text=col.replace("_", " ").title())
            self.members_tree.column(col, width=150)

        self.members_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.refresh_members_table()

    def refresh_members_table(self):
        """Refresh members table"""
        for item in self.members_tree.get_children():
            self.members_tree.delete(item)
        
        members = self.db.get_all_members()
        for member in members:
            self.members_tree.insert("", "end", values=(
                member['member_id'],
                member.get('membership_number', ''),
                f"{member['first_name']} {member['last_name']}",
                member.get('email', ''),
                member.get('phone', ''),
                member.get('status', '')
            ))

    def open_register_member_window(self):
        """Open register member window"""
        win = tk.Toplevel(self)
        win.title("Register New Member")
        win.geometry("500x600")

        tk.Label(win, text="Member Registration", font=("Arial", 16, "bold")).pack(pady=10)

        form_frame = tk.Frame(win)
        form_frame.pack(fill="both", expand=True, padx=30, pady=10)

        fields = [
            ("Membership Number:", "membership_number"),
            ("First Name:", "first_name"),
            ("Last Name:", "last_name"),
            ("Email:", "email"),
            ("Phone:", "phone"),
            ("Address:", "address"),
            ("Membership Type:", "membership_type"),
            ("Status:", "status")
        ]

        entries = {}
        row = 0
        for label_text, key in fields:
            tk.Label(form_frame, text=label_text, font=("Arial", 10)).grid(row=row, column=0, sticky="w", pady=5)
            entry = tk.Entry(form_frame, width=30, font=("Arial", 10))
            entry.grid(row=row, column=1, pady=5)
            entries[key] = entry
            row += 1

        # Set defaults
        entries['membership_type'].insert(0, "Standard")
        entries['status'].insert(0, "Active")

        def save_member():
            try:
                member_data = {
                    'membership_number': entries['membership_number'].get().strip(),
                    'first_name': entries['first_name'].get().strip(),
                    'last_name': entries['last_name'].get().strip(),
                    'email': entries['email'].get().strip(),
                    'phone': entries['phone'].get().strip(),
                    'address': entries['address'].get().strip(),
                    'membership_type': entries['membership_type'].get().strip() or 'Standard',
                    'status': entries['status'].get().strip() or 'Active'
                }

                if not member_data['first_name'] or not member_data['last_name']:
                    messagebox.showerror("Error", "First name and last name are required")
                    return

                self.db.add_member(member_data)
                messagebox.showinfo("Success", "Member registered successfully!")
                self.refresh_members_table()
                self.refresh_dashboard()
                win.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e))
            except Exception as e:
                messagebox.showerror("Error", f"Error registering member: {e}")

        ttk.Button(win, text="Register", command=save_member).pack(pady=10)

    def open_update_member_window(self):
        """Open update member window"""
        selected = self.members_tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a member to update")
            return
        
        item = self.members_tree.item(selected[0])
        member_id = item['values'][0]
        member = self.db.get_member(member_id)
        
        if not member:
            messagebox.showerror("Error", "Member not found")
            return

        win = tk.Toplevel(self)
        win.title("Update Member")
        win.geometry("500x500")

        tk.Label(win, text="Update Member Information", font=("Arial", 16, "bold")).pack(pady=10)

        form_frame = tk.Frame(win)
        form_frame.pack(fill="both", expand=True, padx=30, pady=10)

        fields = [
            ("Email:", "email"),
            ("Phone:", "phone"),
            ("Address:", "address"),
            ("Membership Type:", "membership_type"),
            ("Status:", "status")
        ]

        entries = {}
        row = 0
        for label_text, key in fields:
            tk.Label(form_frame, text=label_text, font=("Arial", 10)).grid(row=row, column=0, sticky="w", pady=5)
            entry = tk.Entry(form_frame, width=30, font=("Arial", 10))
            entry.insert(0, str(member.get(key, '')))
            entry.grid(row=row, column=1, pady=5)
            entries[key] = entry
            row += 1

        def update_member():
            try:
                update_data = {
                    'email': entries['email'].get().strip() or member.get('email'),
                    'phone': entries['phone'].get().strip() or member.get('phone'),
                    'address': entries['address'].get().strip() or member.get('address'),
                    'membership_type': entries['membership_type'].get().strip() or member.get('membership_type'),
                    'status': entries['status'].get().strip() or member.get('status')
                }
                self.db.update_member(member_id, update_data)
                messagebox.showinfo("Success", "Member updated successfully!")
                self.refresh_members_table()
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Error updating member: {e}")

        ttk.Button(win, text="Update", command=update_member).pack(pady=10)

    def open_borrow_history_window(self):
        """Open borrowing history window"""
        selected = self.members_tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a member")
            return
        
        item = self.members_tree.item(selected[0])
        member_id = item['values'][0]

        win = tk.Toplevel(self)
        win.title("Borrowing History")
        win.geometry("800x500")

        history = self.db.get_member_borrowing_history(member_id)
        
        tree = ttk.Treeview(win, columns=("book", "issue_date", "due_date", "return_date", "status"), show="headings", height=15)
        for col in ("book", "issue_date", "due_date", "return_date", "status"):
            tree.heading(col, text=col.replace("_", " ").title())
            tree.column(col, width=150)
        tree.pack(fill="both", expand=True, padx=20, pady=20)

        for record in history:
            tree.insert("", "end", values=(
                record.get('title', ''),
                record.get('issue_date', ''),
                record.get('due_date', ''),
                record.get('return_date', ''),
                record.get('status', '')
            ))

    def open_email_notify_window(self):
        """Open email notification window"""
        win = tk.Toplevel(self)
        win.title("Email Notifications")
        win.geometry("600x500")

        tk.Label(win, text="Email Notification Settings", font=("Arial", 14, "bold")).pack(pady=10)

        # Email config
        config_frame = tk.LabelFrame(win, text="Email Configuration", padx=20, pady=15)
        config_frame.pack(fill="x", padx=20, pady=10)

        tk.Label(config_frame, text="Sender Email:").grid(row=0, column=0, sticky="w", pady=5)
        email_entry = tk.Entry(config_frame, width=40)
        email_entry.grid(row=0, column=1, pady=5)

        tk.Label(config_frame, text="Password:").grid(row=1, column=0, sticky="w", pady=5)
        password_entry = tk.Entry(config_frame, width=40, show="*")
        password_entry.grid(row=1, column=1, pady=5)

        def save_config():
            email = email_entry.get().strip()
            password = password_entry.get().strip()
            if email and password:
                self.notifications.save_email_config(email, password)
                messagebox.showinfo("Success", "Email configuration saved!")
            else:
                messagebox.showerror("Error", "Please enter email and password")

        ttk.Button(config_frame, text="Save Configuration", command=save_config).grid(row=2, column=0, columnspan=2, pady=10)

        # Send reminders
        reminder_frame = tk.LabelFrame(win, text="Send Reminders", padx=20, pady=15)
        reminder_frame.pack(fill="both", expand=True, padx=20, pady=10)

        def send_overdue_reminders():
            overdue = self.db.get_overdue_books()
            if not overdue:
                messagebox.showinfo("Info", "No overdue books")
                return
            
            results = self.notifications.send_bulk_due_reminders(overdue)
            sent_count = sum(1 for r in results if r['sent'])
            messagebox.showinfo("Reminders Sent", f"Sent {sent_count} out of {len(results)} reminders")

        ttk.Button(reminder_frame, text="Send Overdue Reminders", command=send_overdue_reminders).pack(pady=10)

    # ========== TRANSACTION TAB ==========
    def create_transaction_tab(self):
        txn_frame = ttk.Frame(self.notebook)
        self.notebook.add(txn_frame, text="📖 Transactions")

        btn_frame = tk.Frame(txn_frame, bg="#fff3e0")
        btn_frame.pack(fill="x", padx=20, pady=10)
        ttk.Button(btn_frame, text="Issue Book", command=self.open_issue_book_window).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Return Book", command=self.open_return_book_window).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Send Due Date Reminders", command=self.send_due_reminders).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Refresh", command=self.refresh_transactions_table).pack(side="left", padx=5)

        # Transactions table
        table_frame = tk.Frame(txn_frame)
        table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        columns = ("id", "member", "book", "issue_date", "due_date", "return_date", "fine", "status")
        self.transactions_tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.transactions_tree.yview)
        self.transactions_tree.configure(yscrollcommand=scrollbar.set)

        for col in columns:
            self.transactions_tree.heading(col, text=col.replace("_", " ").title())
            self.transactions_tree.column(col, width=120)

        self.transactions_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.refresh_transactions_table()

    def refresh_transactions_table(self):
        """Refresh transactions table"""
        for item in self.transactions_tree.get_children():
            self.transactions_tree.delete(item)
        
        transactions = self.db.get_all_transactions()
        for txn in transactions:
            self.transactions_tree.insert("", "end", values=(
                txn['transaction_id'],
                txn.get('member_name', ''),
                txn.get('book_title', ''),
                txn.get('issue_date', ''),
                txn.get('due_date', ''),
                txn.get('return_date', ''),
                f"${txn.get('fine_amount', 0):.2f}",
                txn.get('status', '')
            ))

    def open_issue_book_window(self):
        """Open issue book window with dropdowns"""
        win = tk.Toplevel(self)
        win.title("Issue Book")
        win.geometry("550x450")

        tk.Label(win, text="Issue Book to Member", font=("Arial", 14, "bold")).pack(pady=10)

        form_frame = tk.Frame(win)
        form_frame.pack(fill="both", expand=True, padx=30, pady=10)

        # Member selection with dropdown
        tk.Label(form_frame, text="Member:", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
        member_var = tk.StringVar()
        members = self.db.get_all_members()
        member_options = [f"{m['member_id']}: {m['first_name']} {m['last_name']} ({m.get('email', '')})" for m in members]
        if not member_options:
            messagebox.showwarning("Warning", "No members available. Please register members first.")
            win.destroy()
            return
        member_combo = ttk.Combobox(form_frame, textvariable=member_var, values=member_options, state="readonly", width=40)
        member_combo.grid(row=0, column=1, pady=5)
        member_combo.current(0)

        # Book selection with dropdown (only available books)
        tk.Label(form_frame, text="Book:", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=5)
        book_var = tk.StringVar()
        books = [b for b in self.db.get_all_books() if b['available_copies'] > 0]
        book_options = [f"{b['book_id']}: {b['title']} by {b['author']} (Available: {b['available_copies']})" for b in books]
        if not book_options:
            messagebox.showwarning("Warning", "No available books. All books are currently issued.")
            win.destroy()
            return
        book_combo = ttk.Combobox(form_frame, textvariable=book_var, values=book_options, state="readonly", width=40)
        book_combo.grid(row=1, column=1, pady=5)
        book_combo.current(0)

        # Issue date
        tk.Label(form_frame, text="Issue Date:", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=5)
        issue_date_entry = tk.Entry(form_frame, width=30, font=("Arial", 10))
        issue_date_entry.insert(0, datetime.now().date().isoformat())
        issue_date_entry.grid(row=2, column=1, pady=5)

        # Due date
        tk.Label(form_frame, text="Due Date:", font=("Arial", 10)).grid(row=3, column=0, sticky="w", pady=5)
        due_date_entry = tk.Entry(form_frame, width=30, font=("Arial", 10))
        due_date_entry.insert(0, (datetime.now().date() + timedelta(days=14)).isoformat())
        due_date_entry.grid(row=3, column=1, pady=5)

        def issue_book():
            try:
                member_id = int(member_var.get().split(":")[0])
                book_id = int(book_var.get().split(":")[0])
                issue_date = issue_date_entry.get().strip()
                due_date = due_date_entry.get().strip()

                # Validate dates
                try:
                    datetime.strptime(issue_date, '%Y-%m-%d')
                    datetime.strptime(due_date, '%Y-%m-%d')
                except ValueError:
                    messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD")
                    return

                # Validate member and book exist
                member = self.db.get_member(member_id)
                book = self.db.get_book(book_id)

                if not member:
                    messagebox.showerror("Error", "Member not found")
                    return
                if not book:
                    messagebox.showerror("Error", "Book not found")
                    return
                if book['available_copies'] <= 0:
                    messagebox.showerror("Error", "Book is not available")
                    return

                self.db.issue_book(member_id, book_id, issue_date, due_date)
                messagebox.showinfo("Success", f"Book '{book['title']}' issued to {member['first_name']} {member['last_name']} successfully!")
                self.refresh_transactions_table()
                self.refresh_books_table()
                self.refresh_dashboard()
                win.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e))
            except Exception as e:
                messagebox.showerror("Error", f"Error issuing book: {e}")

        ttk.Button(win, text="Issue Book", command=issue_book).pack(pady=10)

    def open_return_book_window(self):
        """Open return book window with dropdown"""
        win = tk.Toplevel(self)
        win.title("Return Book")
        win.geometry("550x400")

        tk.Label(win, text="Return Book", font=("Arial", 14, "bold")).pack(pady=10)

        form_frame = tk.Frame(win)
        form_frame.pack(fill="both", expand=True, padx=30, pady=10)

        # Transaction selection with dropdown (only issued books)
        tk.Label(form_frame, text="Transaction:", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
        txn_var = tk.StringVar()
        transactions = [t for t in self.db.get_all_transactions() if t.get('status') == 'Issued' and not t.get('return_date')]
        txn_options = [f"{t['transaction_id']}: {t.get('book_title', '')} - {t.get('member_name', '')} (Due: {t.get('due_date', '')})" for t in transactions]
        if not txn_options:
            messagebox.showinfo("Info", "No books currently issued.")
            win.destroy()
            return
        txn_combo = ttk.Combobox(form_frame, textvariable=txn_var, values=txn_options, state="readonly", width=40)
        txn_combo.grid(row=0, column=1, pady=5)
        txn_combo.current(0)

        tk.Label(form_frame, text="Return Date:", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=5)
        return_date_entry = tk.Entry(form_frame, width=30, font=("Arial", 10))
        return_date_entry.insert(0, datetime.now().date().isoformat())
        return_date_entry.grid(row=1, column=1, pady=5)

        fine_label = tk.Label(form_frame, text="Fine Amount: $0.00", font=("Arial", 10), fg="red")
        fine_label.grid(row=2, column=0, columnspan=2, pady=10)

        def calculate_fine():
            try:
                if not txn_var.get():
                    return
                txn_id = int(txn_var.get().split(":")[0])
                transactions = self.db.get_all_transactions()
                txn = next((t for t in transactions if t['transaction_id'] == txn_id), None)
                
                if not txn:
                    fine_label.config(text="Transaction not found", fg="red")
                    return
                
                if txn.get('return_date'):
                    fine_label.config(text="Book already returned", fg="blue")
                    return

                due_date = datetime.strptime(txn['due_date'], '%Y-%m-%d').date()
                return_date_str = return_date_entry.get().strip()
                if not return_date_str:
                    return
                return_date = datetime.strptime(return_date_str, '%Y-%m-%d').date()
                
                if return_date > due_date:
                    days_overdue = (return_date - due_date).days
                    fine = days_overdue * 1.0  # $1 per day
                    fine_label.config(text=f"Fine Amount: ${fine:.2f} ({days_overdue} days overdue)", fg="red")
                else:
                    fine_label.config(text="Fine Amount: $0.00 (On time)", fg="green")
            except ValueError:
                fine_label.config(text="Invalid date format", fg="red")
            except:
                pass

        txn_combo.bind("<<ComboboxSelected>>", lambda e: calculate_fine())
        return_date_entry.bind("<KeyRelease>", lambda e: calculate_fine())

        def return_book():
            try:
                if not txn_var.get():
                    messagebox.showerror("Error", "Please select a transaction")
                    return
                txn_id = int(txn_var.get().split(":")[0])
                return_date = return_date_entry.get().strip()

                if not return_date:
                    messagebox.showerror("Error", "Please enter return date")
                    return

                # Validate date format
                try:
                    datetime.strptime(return_date, '%Y-%m-%d')
                except ValueError:
                    messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD")
                    return

                # Calculate fine
                transactions = self.db.get_all_transactions()
                txn = next((t for t in transactions if t['transaction_id'] == txn_id), None)
                
                if not txn:
                    messagebox.showerror("Error", "Transaction not found")
                    return

                if txn.get('return_date'):
                    messagebox.showwarning("Warning", "Book already returned")
                    return

                due_date = datetime.strptime(txn['due_date'], '%Y-%m-%d').date()
                return_date_obj = datetime.strptime(return_date, '%Y-%m-%d').date()
                
                fine = 0
                if return_date_obj > due_date:
                    days_overdue = (return_date_obj - due_date).days
                    fine = days_overdue * 1.0

                self.db.return_book(txn_id, return_date, fine)
                fine_msg = f"\nFine: ${fine:.2f}" if fine > 0 else "\nNo fine (returned on time)"
                messagebox.showinfo("Success", f"Book '{txn.get('book_title', '')}' returned successfully!{fine_msg}")
                self.refresh_transactions_table()
                self.refresh_books_table()
                self.refresh_dashboard()
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Error returning book: {e}")

        ttk.Button(win, text="Return Book", command=return_book).pack(pady=10)

    def send_due_reminders(self):
        """Send due date reminders"""
        overdue = self.db.get_overdue_books()
        if not overdue:
            messagebox.showinfo("Info", "No overdue books")
            return
        
        results = self.notifications.send_bulk_due_reminders(overdue)
        sent_count = sum(1 for r in results if r['sent'])
        messagebox.showinfo("Reminders Sent", f"Sent {sent_count} out of {len(results)} reminders")

    # ========== REVIEWS TAB ==========
    def create_reviews_tab(self):
        review_frame = ttk.Frame(self.notebook)
        self.notebook.add(review_frame, text="⭐ Reviews")

        # Title and add review section
        header_frame = tk.Frame(review_frame, bg="#f5f5f5")
        header_frame.pack(fill="x", padx=20, pady=10)
        
        tk.Label(header_frame, text="Book Reviews", font=("Arial", 16, "bold"), bg="#f5f5f5").pack(side="left", padx=10)
        ttk.Button(header_frame, text="Add Review", command=self.open_add_review_window).pack(side="right", padx=10)
        ttk.Button(header_frame, text="Refresh", command=self.refresh_reviews_table).pack(side="right", padx=5)

        # Filter frame
        filter_frame = tk.Frame(review_frame, bg="#f5f5f5")
        filter_frame.pack(fill="x", padx=20, pady=5)
        
        tk.Label(filter_frame, text="Filter by Book:", bg="#f5f5f5", font=("Arial", 10)).pack(side="left", padx=5)
        book_filter_var = tk.StringVar(value="All Books")
        books_list = ["All Books"] + [f"{b['book_id']}: {b['title']}" for b in self.db.get_all_books()]
        book_filter = ttk.Combobox(filter_frame, textvariable=book_filter_var, values=books_list, state="readonly", width=40)
        book_filter.pack(side="left", padx=5)
        
        def filter_reviews():
            self.refresh_reviews_table(book_filter_var.get())
        
        ttk.Button(filter_frame, text="Filter", command=filter_reviews).pack(side="left", padx=5)

        # Reviews display
        table_frame = tk.Frame(review_frame)
        table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        columns = ("book", "member", "rating", "review", "date")
        self.reviews_tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.reviews_tree.yview)
        self.reviews_tree.configure(yscrollcommand=scrollbar.set)

        for col in columns:
            self.reviews_tree.heading(col, text=col.title())
            if col == "review":
                self.reviews_tree.column(col, width=300)
            else:
                self.reviews_tree.column(col, width=120)

        self.reviews_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Store filter for refresh
        self.reviews_book_filter = book_filter_var

        # Initial load
        self.refresh_reviews_table()

    def refresh_reviews_table(self, filter_book="All Books"):
        """Refresh reviews table"""
        for item in self.reviews_tree.get_children():
            self.reviews_tree.delete(item)
        
        # Get all reviews
        all_books = self.db.get_all_books()
        all_reviews = []
        
        for book in all_books:
            reviews = self.db.get_book_reviews(book['book_id'])
            for review in reviews:
                review['book_title'] = book['title']
                all_reviews.append(review)
        
        # Filter if needed
        if filter_book != "All Books":
            book_id = int(filter_book.split(":")[0])
            all_reviews = [r for r in all_reviews if r['book_id'] == book_id]
        
        # Display reviews
        for review in all_reviews:
            rating_stars = "⭐" * review['rating'] + "☆" * (5 - review['rating'])
            review_text = review.get('review_text', '')[:100] + "..." if len(review.get('review_text', '')) > 100 else review.get('review_text', '')
            self.reviews_tree.insert("", "end", values=(
                review.get('book_title', ''),
                review.get('member_name', ''),
                rating_stars,
                review_text,
                review.get('review_date', '')
            ))

    def open_add_review_window(self):
        """Open add review window with dropdowns"""
        win = tk.Toplevel(self)
        win.title("Add Book Review")
        win.geometry("500x400")

        tk.Label(win, text="Add Book Review", font=("Arial", 16, "bold")).pack(pady=10)

        form_frame = tk.Frame(win)
        form_frame.pack(fill="both", expand=True, padx=30, pady=10)

        # Book selection
        tk.Label(form_frame, text="Book:", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
        book_var = tk.StringVar()
        books = self.db.get_all_books()
        book_options = [f"{b['book_id']}: {b['title']}" for b in books]
        if not book_options:
            messagebox.showwarning("Warning", "No books available. Please add books first.")
            win.destroy()
            return
        book_combo = ttk.Combobox(form_frame, textvariable=book_var, values=book_options, state="readonly", width=35)
        book_combo.grid(row=0, column=1, pady=5)
        book_combo.current(0)

        # Member selection
        tk.Label(form_frame, text="Member:", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=5)
        member_var = tk.StringVar()
        members = self.db.get_all_members()
        member_options = [f"{m['member_id']}: {m['first_name']} {m['last_name']}" for m in members]
        if not member_options:
            messagebox.showwarning("Warning", "No members available. Please register members first.")
            win.destroy()
            return
        member_combo = ttk.Combobox(form_frame, textvariable=member_var, values=member_options, state="readonly", width=35)
        member_combo.grid(row=1, column=1, pady=5)
        member_combo.current(0)

        # Rating
        tk.Label(form_frame, text="Rating (1-5):", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=5)
        rating_var = tk.IntVar(value=5)
        rating_frame = tk.Frame(form_frame)
        rating_frame.grid(row=2, column=1, pady=5, sticky="w")
        for i in range(1, 6):
            tk.Radiobutton(rating_frame, text=str(i), variable=rating_var, value=i, font=("Arial", 10)).pack(side="left", padx=5)

        # Review text
        tk.Label(form_frame, text="Review:", font=("Arial", 10)).grid(row=3, column=0, sticky="nw", pady=5)
        review_text = scrolledtext.ScrolledText(form_frame, width=35, height=8, font=("Arial", 10))
        review_text.grid(row=3, column=1, pady=5)

        def save_review():
            try:
                book_id = int(book_var.get().split(":")[0])
                member_id = int(member_var.get().split(":")[0])
                rating = rating_var.get()
                review = review_text.get("1.0", tk.END).strip()

                if not review:
                    messagebox.showerror("Error", "Please enter a review")
                    return

                self.db.add_review(book_id, member_id, rating, review)
                messagebox.showinfo("Success", "Review added successfully!")
                self.refresh_reviews_table()
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Error adding review: {e}")

        ttk.Button(win, text="Save Review", command=save_review).pack(pady=10)


if __name__ == "__main__":
    app = LibraryManagementSystem()
    app.mainloop()

