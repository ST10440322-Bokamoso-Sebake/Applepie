<<<<<<< HEAD
# Library Management System

A comprehensive Library Management System with database integration, GUI interface, and API integration for automatic book data retrieval.

## Features

### 1. Database Design ✅
- **Books Table**: Complete book information with ISBN, title, author, publisher, publication year, category, description, cover image URL, page count, language, copies, and shelf location
- **Members Table**: Member information with membership number, name, email, phone, address, join date, membership type, and status
- **Transactions Table**: Book issue/return tracking with dates, fines, and status
- **Book Reviews Table**: Rating and review system for books

### 2. GUI Features ✅

#### Dashboard
- Real-time key statistics (total books, members, issued books, available books, overdue books)
- Quick action buttons for common tasks
- Recent transactions list
- Popular books widget

#### Book Management with API Integration
- **Add New Books**: ISBN lookup with automatic data population from Google Books API and Open Library API
- **Auto-populate**: Book details automatically filled from API (title, author, publisher, description, cover image, etc.)
- **Display Cover Images**: Book cover images displayed when available
- **Update Book Details**: Modify book information and availability
- **Search Books**: Search by title, author, ISBN, or category
- **View Availability**: See available copies vs total copies

#### Member Management
- **Register New Members**: Complete member registration form
- **Update Member Information**: Modify member details
- **View Borrowing History**: See all books borrowed by a member
- **Email Notifications**: Send email reminders and notifications

#### Transaction Management
- **Issue Books**: Issue books to members with automatic due date calculation
- **Return Books**: Process returns with automatic fine calculation ($1/day overdue)
- **View All Transactions**: Complete transaction history
- **Due Date Reminders**: Send email reminders for overdue books

### 3. API Integration Features ✅

#### Google Books API Integration
- ISBN lookup to auto-fill book details
- Fetch book cover images
- Get book descriptions and metadata
- Search for books by title/author

#### Open Library API Integration
- Alternative source for book information
- Get author information
- Fetch related books/recommendations
- Fallback when Google Books doesn't have the book

#### Email/SMS Notification API
- Send due date reminders
- Overdue book notifications
- New book arrival notifications (ready for implementation)
- Email configuration interface

## Installation

1. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   python main.py
   ```

## Project Structure

```
Programming_Project/
├── main.py                 # Main GUI application (integrated system)
├── db_manager.py           # Database operations module
├── book_api.py            # Google Books & Open Library API integration
├── notifications.py       # Email/SMS notification module
├── requirements.txt       # Python dependencies
├── library.db             # SQLite database (created automatically)
├── email_config.json       # Email configuration (created when configured)
└── README.md              # This file
```

## Usage Guide

### Starting the Application

Run `python main.py` to launch the Library Management System GUI.

### Adding Books with ISBN Lookup

1. Go to **Book Management** tab
2. Click **"Add New Book (ISBN Lookup)"**
3. Enter an ISBN (e.g., "9780143127741" for "The Great Gatsby")
4. Click **"Lookup"** - the system will automatically fetch book details from APIs
5. Review and adjust the auto-populated fields
6. Enter additional details (total copies, shelf location)
7. Click **"Save Book"**

### Registering Members

1. Go to **Member Management** tab
2. Click **"Register New Member"**
3. Fill in member details
4. Click **"Register"**

### Issuing Books

1. Go to **Transactions** tab
2. Click **"Issue Book"**
3. Enter Member ID and Book ID
4. Issue date and due date are auto-filled (can be modified)
5. Click **"Issue Book"**

### Returning Books

1. Go to **Transactions** tab
2. Click **"Return Book"**
3. Enter Transaction ID
4. Return date is auto-filled (can be modified)
5. Fine is automatically calculated if overdue
6. Click **"Return Book"**

### Searching Books

1. Go to **Book Management** tab
2. Click **"Search Books"**
3. Enter search term and select search type (title, author, ISBN, category)
4. Click **"Search"**

### Setting Up Email Notifications

1. Go to **Member Management** tab
2. Click **"Send Email Notifications"**
3. Enter your email and password (Gmail recommended)
4. Click **"Save Configuration"**
5. Use **"Send Overdue Reminders"** to send bulk reminders

**Note**: For Gmail, you may need to use an "App Password" instead of your regular password. Enable 2-factor authentication and generate an app password.

## API Integration Details

### Google Books API
- **No API Key Required**: Free public API
- **Rate Limits**: 1000 requests per day
- **Features**: ISBN lookup, book search, cover images, descriptions

### Open Library API
- **No API Key Required**: Free public API
- **Features**: Alternative book data source, author information, related books

### Email Notifications
- **SMTP Configuration**: Supports Gmail and other SMTP servers
- **Default Settings**: Gmail SMTP (smtp.gmail.com, port 587)
- **Security**: Uses TLS encryption

## Database Schema

The system automatically creates the following tables:

- **books**: Book information and inventory
- **members**: Member registration and details
- **transactions**: Book issue/return records
- **book_reviews**: Book ratings and reviews

## Features by Tab

### 📊 Dashboard
- Statistics overview
- Quick actions
- Recent transactions
- Popular books

### 📚 Book Management
- Add books (with ISBN lookup)
- Search books
- Update book details
- View all books

### 👥 Member Management
- Register members
- Update member info
- View borrowing history
- Email notifications

### 📖 Transactions
- Issue books
- Return books
- View all transactions
- Send due date reminders

### ⭐ Reviews
- Add book reviews
- View reviews (placeholder for display)

## Troubleshooting

### Email Not Working
- Check email configuration in "Send Email Notifications"
- For Gmail, use an App Password (not regular password)
- Ensure SMTP server and port are correct

### ISBN Lookup Not Working
- Check internet connection
- Try a different ISBN format (with or without hyphens)
- The system tries Google Books first, then Open Library

### Database Errors
- Ensure you have write permissions in the project directory
- The database file (library.db) is created automatically

## Future Enhancements

- SMS notification integration (Twilio, AWS SNS)
- Book review display and management
- Advanced reporting and analytics
- Export functionality (CSV, PDF)
- Barcode scanning support
- Multi-user authentication

## Requirements

- Python 3.7+
- tkinter (usually included with Python)
- Pillow (for image handling)
- requests (for API calls)

## License

This project is for educational purposes.

## Authors

Neo & Olwethu

---

**Note**: This system integrates all three parts (Database, GUI, and API Integration) into a unified, working application.
=======
# BabyWethu
Assignment submission helping with itergration
>>>>>>> 08e542488fdd7c8e5fd4ffd39e027576baf8a069
