"""
Database Manager Module
Handles all database operations for the Library Management System
"""
import sqlite3
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple


class DatabaseManager:
    def __init__(self, db_name: str = "library.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = sqlite3.Row  # Enable column access by name
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Create all required tables if they don't exist"""
        # Books Table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                isbn TEXT UNIQUE,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                publisher TEXT,
                publication_year INTEGER,
                category TEXT,
                description TEXT,
                cover_image_url TEXT,
                page_count INTEGER,
                language TEXT,
                total_copies INTEGER DEFAULT 1,
                available_copies INTEGER DEFAULT 1,
                shelf_location TEXT
            )
        """)

        # Members Table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS members (
                member_id INTEGER PRIMARY KEY AUTOINCREMENT,
                membership_number TEXT UNIQUE,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT UNIQUE,
                phone TEXT,
                address TEXT,
                join_date DATE,
                membership_type TEXT,
                status TEXT DEFAULT 'Active'
            )
        """)

        # Transactions Table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                member_id INTEGER,
                book_id INTEGER,
                issue_date DATE,
                due_date DATE,
                return_date DATE,
                fine_amount REAL DEFAULT 0,
                status TEXT DEFAULT 'Issued',
                FOREIGN KEY(member_id) REFERENCES members(member_id),
                FOREIGN KEY(book_id) REFERENCES books(book_id)
            )
        """)

        # Book Reviews Table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS book_reviews (
                review_id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id INTEGER,
                member_id INTEGER,
                rating INTEGER NOT NULL CHECK(rating >= 1 AND rating <= 5),
                review_text TEXT,
                review_date DATE,
                FOREIGN KEY(book_id) REFERENCES books(book_id),
                FOREIGN KEY(member_id) REFERENCES members(member_id)
            )
        """)

        self.conn.commit()

    # ========== BOOK OPERATIONS ==========
    def add_book(self, book_data: Dict) -> int:
        """Add a new book to the database"""
        try:
            self.cursor.execute("""
                INSERT INTO books (
                    isbn, title, author, publisher, publication_year, category,
                    description, cover_image_url, page_count, language,
                    total_copies, available_copies, shelf_location
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                book_data.get('isbn'),
                book_data.get('title', ''),
                book_data.get('author', ''),
                book_data.get('publisher', ''),
                book_data.get('publication_year'),
                book_data.get('category', ''),
                book_data.get('description', ''),
                book_data.get('cover_image_url', ''),
                book_data.get('page_count', 0),
                book_data.get('language', ''),
                book_data.get('total_copies', 1),
                book_data.get('available_copies', book_data.get('total_copies', 1)),
                book_data.get('shelf_location', '')
            ))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("Book with this ISBN already exists")

    def update_book(self, book_id: int, book_data: Dict):
        """Update book information"""
        fields = []
        values = []
        for key, value in book_data.items():
            if value is not None:
                fields.append(f"{key} = ?")
                values.append(value)
        values.append(book_id)
        
        if fields:
            query = f"UPDATE books SET {', '.join(fields)} WHERE book_id = ?"
            self.cursor.execute(query, values)
            self.conn.commit()

    def get_book(self, book_id: int) -> Optional[Dict]:
        """Get book by ID"""
        self.cursor.execute("SELECT * FROM books WHERE book_id = ?", (book_id,))
        row = self.cursor.fetchone()
        return dict(row) if row else None

    def search_books(self, search_term: str = "", search_by: str = "title") -> List[Dict]:
        """Search books by title, author, ISBN, or category"""
        if search_by == "title":
            query = "SELECT * FROM books WHERE title LIKE ?"
        elif search_by == "author":
            query = "SELECT * FROM books WHERE author LIKE ?"
        elif search_by == "isbn":
            query = "SELECT * FROM books WHERE isbn LIKE ?"
        elif search_by == "category":
            query = "SELECT * FROM books WHERE category LIKE ?"
        else:
            query = "SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR isbn LIKE ?"
            self.cursor.execute(query, (f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"))
            rows = self.cursor.fetchall()
            return [dict(row) for row in rows]
        
        self.cursor.execute(query, (f"%{search_term}%",))
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]

    def get_all_books(self) -> List[Dict]:
        """Get all books"""
        self.cursor.execute("SELECT * FROM books")
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]

    def get_popular_books(self, limit: int = 5) -> List[Dict]:
        """Get most borrowed books"""
        self.cursor.execute("""
            SELECT b.*, COUNT(t.transaction_id) as borrow_count
            FROM books b
            LEFT JOIN transactions t ON b.book_id = t.book_id
            GROUP BY b.book_id
            ORDER BY borrow_count DESC
            LIMIT ?
        """, (limit,))
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]

    # ========== MEMBER OPERATIONS ==========
    def add_member(self, member_data: Dict) -> int:
        """Add a new member"""
        try:
            self.cursor.execute("""
                INSERT INTO members (
                    membership_number, first_name, last_name, email, phone,
                    address, join_date, membership_type, status
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                member_data.get('membership_number'),
                member_data.get('first_name', ''),
                member_data.get('last_name', ''),
                member_data.get('email', ''),
                member_data.get('phone', ''),
                member_data.get('address', ''),
                member_data.get('join_date', datetime.now().date().isoformat()),
                member_data.get('membership_type', 'Standard'),
                member_data.get('status', 'Active')
            ))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError as e:
            if 'email' in str(e):
                raise ValueError("Member with this email already exists")
            elif 'membership_number' in str(e):
                raise ValueError("Member with this membership number already exists")
            raise

    def update_member(self, member_id: int, member_data: Dict):
        """Update member information"""
        fields = []
        values = []
        for key, value in member_data.items():
            if value is not None:
                fields.append(f"{key} = ?")
                values.append(value)
        values.append(member_id)
        
        if fields:
            query = f"UPDATE members SET {', '.join(fields)} WHERE member_id = ?"
            self.cursor.execute(query, values)
            self.conn.commit()

    def get_member(self, member_id: int) -> Optional[Dict]:
        """Get member by ID"""
        self.cursor.execute("SELECT * FROM members WHERE member_id = ?", (member_id,))
        row = self.cursor.fetchone()
        return dict(row) if row else None

    def get_member_by_email(self, email: str) -> Optional[Dict]:
        """Get member by email"""
        self.cursor.execute("SELECT * FROM members WHERE email = ?", (email,))
        row = self.cursor.fetchone()
        return dict(row) if row else None

    def get_all_members(self) -> List[Dict]:
        """Get all members"""
        self.cursor.execute("SELECT * FROM members")
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]

    def get_member_borrowing_history(self, member_id: int) -> List[Dict]:
        """Get borrowing history for a member"""
        self.cursor.execute("""
            SELECT t.*, b.title, b.author, b.isbn
            FROM transactions t
            JOIN books b ON t.book_id = b.book_id
            WHERE t.member_id = ?
            ORDER BY t.issue_date DESC
        """, (member_id,))
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]

    # ========== TRANSACTION OPERATIONS ==========
    def issue_book(self, member_id: int, book_id: int, issue_date: str = None, due_date: str = None) -> int:
        """Issue a book to a member"""
        if issue_date is None:
            issue_date = datetime.now().date().isoformat()
        if due_date is None:
            due_date = (datetime.now().date() + timedelta(days=14)).isoformat()
        
        # Check if book is available
        book = self.get_book(book_id)
        if not book or book['available_copies'] <= 0:
            raise ValueError("Book is not available")
        
        # Create transaction
        self.cursor.execute("""
            INSERT INTO transactions (member_id, book_id, issue_date, due_date, status)
            VALUES (?, ?, ?, ?, 'Issued')
        """, (member_id, book_id, issue_date, due_date))
        
        # Update available copies
        self.cursor.execute("""
            UPDATE books SET available_copies = available_copies - 1
            WHERE book_id = ?
        """, (book_id,))
        
        self.conn.commit()
        return self.cursor.lastrowid

    def return_book(self, transaction_id: int, return_date: str = None, fine_amount: float = 0):
        """Return a book and calculate fine"""
        if return_date is None:
            return_date = datetime.now().date().isoformat()
        
        # Get transaction
        self.cursor.execute("SELECT * FROM transactions WHERE transaction_id = ?", (transaction_id,))
        txn = self.cursor.fetchone()
        if not txn:
            raise ValueError("Transaction not found")
        
        txn_dict = dict(txn)
        
        # Update transaction
        self.cursor.execute("""
            UPDATE transactions
            SET return_date = ?, fine_amount = ?, status = 'Returned'
            WHERE transaction_id = ?
        """, (return_date, fine_amount, transaction_id))
        
        # Update available copies
        self.cursor.execute("""
            UPDATE books SET available_copies = available_copies + 1
            WHERE book_id = ?
        """, (txn_dict['book_id'],))
        
        self.conn.commit()

    def get_all_transactions(self) -> List[Dict]:
        """Get all transactions with book and member details"""
        self.cursor.execute("""
            SELECT t.*, b.title as book_title, b.author,
                   m.first_name || ' ' || m.last_name as member_name, m.email
            FROM transactions t
            JOIN books b ON t.book_id = b.book_id
            JOIN members m ON t.member_id = m.member_id
            ORDER BY t.issue_date DESC
        """)
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]

    def get_overdue_books(self) -> List[Dict]:
        """Get all overdue books"""
        today = datetime.now().date().isoformat()
        self.cursor.execute("""
            SELECT t.*, b.title as book_title, b.author,
                   m.first_name || ' ' || m.last_name as member_name, m.email, m.phone
            FROM transactions t
            JOIN books b ON t.book_id = b.book_id
            JOIN members m ON t.member_id = m.member_id
            WHERE t.status = 'Issued' AND t.due_date < ? AND t.return_date IS NULL
        """, (today,))
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]

    def get_recent_transactions(self, limit: int = 10) -> List[Dict]:
        """Get recent transactions"""
        self.cursor.execute("""
            SELECT t.*, b.title as book_title,
                   m.first_name || ' ' || m.last_name as member_name
            FROM transactions t
            JOIN books b ON t.book_id = b.book_id
            JOIN members m ON t.member_id = m.member_id
            ORDER BY t.issue_date DESC
            LIMIT ?
        """, (limit,))
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]

    # ========== REVIEW OPERATIONS ==========
    def add_review(self, book_id: int, member_id: int, rating: int, review_text: str) -> int:
        """Add a book review"""
        self.cursor.execute("""
            INSERT INTO book_reviews (book_id, member_id, rating, review_text, review_date)
            VALUES (?, ?, ?, ?, ?)
        """, (book_id, member_id, rating, review_text, datetime.now().date().isoformat()))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_book_reviews(self, book_id: int) -> List[Dict]:
        """Get all reviews for a book"""
        self.cursor.execute("""
            SELECT r.*, m.first_name || ' ' || m.last_name as member_name
            FROM book_reviews r
            JOIN members m ON r.member_id = m.member_id
            WHERE r.book_id = ?
            ORDER BY r.review_date DESC
        """, (book_id,))
        rows = self.cursor.fetchall()
        return [dict(row) for row in rows]

    # ========== STATISTICS ==========
    def get_statistics(self) -> Dict:
        """Get library statistics"""
        stats = {}
        
        # Total books
        self.cursor.execute("SELECT COUNT(*) FROM books")
        stats['total_books'] = self.cursor.fetchone()[0]
        
        # Total members
        self.cursor.execute("SELECT COUNT(*) FROM members")
        stats['total_members'] = self.cursor.fetchone()[0]
        
        # Books issued
        self.cursor.execute("SELECT COUNT(*) FROM transactions WHERE status = 'Issued'")
        stats['books_issued'] = self.cursor.fetchone()[0]
        
        # Available books
        self.cursor.execute("SELECT SUM(available_copies) FROM books")
        stats['available_books'] = self.cursor.fetchone()[0] or 0
        
        # Overdue books
        today = datetime.now().date().isoformat()
        self.cursor.execute("""
            SELECT COUNT(*) FROM transactions
            WHERE status = 'Issued' AND due_date < ? AND return_date IS NULL
        """, (today,))
        stats['overdue_books'] = self.cursor.fetchone()[0]
        
        return stats

    def close(self):
        """Close database connection"""
        self.conn.close()

