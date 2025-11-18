"""
Notification Module
Handles email and SMS notifications for the Library Management System
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
from typing import List, Dict
import json


class NotificationManager:
    def __init__(self, smtp_server: str = "smtp.gmail.com", smtp_port: int = 587):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email_config = self._load_email_config()
        self.sms_config = self._load_sms_config()

    def _load_email_config(self) -> Dict:
        """Load email configuration from file or use defaults"""
        try:
            with open('email_config.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            # Return default config (user needs to set up)
            return {
                'enabled': False,
                'sender_email': '',
                'sender_password': '',
                'smtp_server': self.smtp_server,
                'smtp_port': self.smtp_port
            }

    def _load_sms_config(self) -> Dict:
        """Load SMS configuration from file or use defaults"""
        try:
            with open('sms_config.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                'enabled': False,
                'api_key': '',
                'api_secret': '',
                'from_number': ''
            }

    def save_email_config(self, email: str, password: str):
        """Save email configuration"""
        config = {
            'enabled': True,
            'sender_email': email,
            'sender_password': password,
            'smtp_server': self.smtp_server,
            'smtp_port': self.smtp_port
        }
        with open('email_config.json', 'w') as f:
            json.dump(config, f, indent=2)
        self.email_config = config

    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        """Send email notification"""
        if not self.email_config.get('enabled'):
            print(f"[EMAIL NOT SENT - Config not set] To: {recipient}, Subject: {subject}")
            return False
        
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email_config['sender_email']
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
            
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.email_config['sender_email'], self.email_config['sender_password'])
            server.send_message(msg)
            server.quit()
            
            print(f"Email sent successfully to {recipient}")
            return True
        except Exception as e:
            print(f"Error sending email: {e}")
            return False

    def send_sms(self, phone_number: str, message: str) -> bool:
        """Send SMS notification (placeholder - requires SMS API service)"""
        if not self.sms_config.get('enabled'):
            print(f"[SMS NOT SENT - Config not set] To: {phone_number}, Message: {message[:50]}...")
            return False
        
        # This is a placeholder. In production, you would integrate with:
        # - Twilio API
        # - AWS SNS
        # - Other SMS service providers
        print(f"[SMS] To: {phone_number}, Message: {message}")
        return True

    def send_due_date_reminder(self, member_email: str, member_name: str, book_title: str, due_date: str):
        """Send due date reminder email"""
        subject = "Library Book Due Date Reminder"
        body = f"""
Dear {member_name},

This is a reminder that the book "{book_title}" is due on {due_date}.

Please return the book on or before the due date to avoid late fees.

Thank you,
Library Management System
        """.strip()
        return self.send_email(member_email, subject, body)

    def send_overdue_notification(self, member_email: str, member_name: str, book_title: str, 
                                   due_date: str, days_overdue: int, fine_amount: float):
        """Send overdue book notification"""
        subject = "Overdue Book Notification"
        body = f"""
Dear {member_name},

The book "{book_title}" is overdue.

Due Date: {due_date}
Days Overdue: {days_overdue}
Fine Amount: ${fine_amount:.2f}

Please return the book as soon as possible to avoid additional charges.

Thank you,
Library Management System
        """.strip()
        return self.send_email(member_email, subject, body)

    def send_new_book_notification(self, member_email: str, member_name: str, book_title: str, author: str):
        """Send new book arrival notification"""
        subject = "New Book Arrival"
        body = f"""
Dear {member_name},

We're excited to inform you that a new book has arrived at the library:

Title: {book_title}
Author: {author}

Visit the library to check it out!

Thank you,
Library Management System
        """.strip()
        return self.send_email(member_email, subject, body)

    def send_bulk_due_reminders(self, overdue_list: List[Dict]):
        """Send reminders to multiple members"""
        results = []
        for item in overdue_list:
            member_email = item.get('email', '')
            member_name = item.get('member_name', 'Member')
            book_title = item.get('book_title', 'Book')
            due_date = item.get('due_date', '')
            
            # Calculate days overdue
            try:
                due = datetime.strptime(due_date, '%Y-%m-%d').date()
                days_overdue = (datetime.now().date() - due).days
            except:
                days_overdue = 0
            
            if days_overdue > 0:
                result = self.send_overdue_notification(
                    member_email, member_name, book_title, due_date, days_overdue, 0
                )
            else:
                result = self.send_due_date_reminder(member_email, member_name, book_title, due_date)
            
            results.append({
                'member': member_name,
                'email': member_email,
                'sent': result
            })
        
        return results

    def send_sms_reminder(self, phone_number: str, book_title: str, due_date: str):
        """Send SMS reminder"""
        message = f"Reminder: '{book_title}' is due on {due_date}. Please return to library."
        return self.send_sms(phone_number, message)

