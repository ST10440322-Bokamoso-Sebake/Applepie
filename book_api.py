"""
Book API Integration Module
Handles Google Books API and Open Library API integration
"""
import requests
import json
from typing import Dict, List, Optional
from urllib.parse import quote


class BookAPI:
    def __init__(self):
        self.google_books_base = "https://www.googleapis.com/books/v1/volumes"
        self.open_library_base = "https://openlibrary.org"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Library Management System/1.0'
        })

    def search_google_books(self, query: str, max_results: int = 10) -> List[Dict]:
        """Search Google Books API"""
        try:
            url = f"{self.google_books_base}?q={quote(query)}&maxResults={max_results}"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            books = []
            for item in data.get('items', []):
                book_info = self._parse_google_book(item)
                if book_info:
                    books.append(book_info)
            return books
        except Exception as e:
            print(f"Error searching Google Books: {e}")
            return []

    def get_book_by_isbn(self, isbn: str) -> Optional[Dict]:
        """Get book information by ISBN from Google Books"""
        try:
            # Remove hyphens and spaces from ISBN
            clean_isbn = isbn.replace('-', '').replace(' ', '')
            url = f"{self.google_books_base}?q=isbn:{clean_isbn}"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if data.get('totalItems', 0) > 0:
                return self._parse_google_book(data['items'][0])
            return None
        except Exception as e:
            print(f"Error fetching book by ISBN from Google Books: {e}")
            return None

    def _parse_google_book(self, item: Dict) -> Optional[Dict]:
        """Parse Google Books API response"""
        try:
            volume_info = item.get('volumeInfo', {})
            
            # Extract ISBNs
            isbn_13 = None
            isbn_10 = None
            for identifier in volume_info.get('industryIdentifiers', []):
                if identifier.get('type') == 'ISBN_13':
                    isbn_13 = identifier.get('identifier')
                elif identifier.get('type') == 'ISBN_10':
                    isbn_10 = identifier.get('identifier')
            
            isbn = isbn_13 or isbn_10 or ''
            
            # Extract authors
            authors = volume_info.get('authors', [])
            author = ', '.join(authors) if authors else 'Unknown'
            
            # Extract categories
            categories = volume_info.get('categories', [])
            category = categories[0] if categories else 'General'
            
            # Extract description
            description = volume_info.get('description', '')
            if description and len(description) > 1000:
                description = description[:1000] + '...'
            
            # Extract image
            image_links = volume_info.get('imageLinks', {})
            cover_image = image_links.get('thumbnail', '') or image_links.get('smallThumbnail', '')
            if cover_image:
                # Replace http with https and increase image size
                cover_image = cover_image.replace('http://', 'https://')
                cover_image = cover_image.replace('zoom=1', 'zoom=2')
            
            # Extract publication date
            published_date = volume_info.get('publishedDate', '')
            publication_year = None
            if published_date:
                try:
                    publication_year = int(published_date[:4])
                except:
                    pass
            
            book_data = {
                'isbn': isbn,
                'title': volume_info.get('title', ''),
                'author': author,
                'publisher': volume_info.get('publisher', ''),
                'publication_year': publication_year,
                'category': category,
                'description': description,
                'cover_image_url': cover_image,
                'page_count': volume_info.get('pageCount', 0),
                'language': volume_info.get('language', 'en'),
                'total_copies': 1,  # Default, can be updated
                'available_copies': 1,
                'shelf_location': ''
            }
            
            return book_data
        except Exception as e:
            print(f"Error parsing Google Books data: {e}")
            return None

    def search_open_library(self, query: str, max_results: int = 10) -> List[Dict]:
        """Search Open Library API"""
        try:
            url = f"{self.open_library_base}/search.json?q={quote(query)}&limit={max_results}"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            books = []
            for doc in data.get('docs', []):
                book_info = self._parse_open_library_book(doc)
                if book_info:
                    books.append(book_info)
            return books
        except Exception as e:
            print(f"Error searching Open Library: {e}")
            return []

    def get_book_by_isbn_open_library(self, isbn: str) -> Optional[Dict]:
        """Get book information by ISBN from Open Library"""
        try:
            clean_isbn = isbn.replace('-', '').replace(' ', '')
            url = f"{self.open_library_base}/isbn/{clean_isbn}.json"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            return self._parse_open_library_book(data)
        except Exception as e:
            print(f"Error fetching book by ISBN from Open Library: {e}")
            return None

    def _parse_open_library_book(self, doc: Dict) -> Optional[Dict]:
        """Parse Open Library API response"""
        try:
            # Extract ISBN
            isbn_list = doc.get('isbn', [])
            isbn = isbn_list[0] if isbn_list else ''
            
            # Extract authors
            authors = doc.get('author_name', [])
            author = ', '.join(authors) if authors else 'Unknown'
            
            # Extract categories/subjects
            subjects = doc.get('subject', [])
            category = subjects[0] if subjects else 'General'
            
            # Extract cover image
            cover_id = doc.get('cover_i')
            cover_image = f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg" if cover_id else ''
            
            # Extract publication year
            publish_year = doc.get('first_publish_year') or doc.get('publish_year', [None])[0]
            publication_year = None
            if publish_year:
                try:
                    publication_year = int(publish_year)
                except:
                    pass
            
            book_data = {
                'isbn': isbn,
                'title': doc.get('title', ''),
                'author': author,
                'publisher': ', '.join(doc.get('publisher', [])) if doc.get('publisher') else '',
                'publication_year': publication_year,
                'category': category,
                'description': doc.get('first_sentence', [''])[0] if doc.get('first_sentence') else '',
                'cover_image_url': cover_image,
                'page_count': doc.get('number_of_pages_median', 0) or doc.get('number_of_pages', [0])[0] if doc.get('number_of_pages') else 0,
                'language': doc.get('language', ['en'])[0] if doc.get('language') else 'en',
                'total_copies': 1,
                'available_copies': 1,
                'shelf_location': ''
            }
            
            return book_data
        except Exception as e:
            print(f"Error parsing Open Library data: {e}")
            return None

    def get_author_info(self, author_name: str) -> Optional[Dict]:
        """Get author information from Open Library"""
        try:
            url = f"{self.open_library_base}/search/authors.json?q={quote(author_name)}&limit=1"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if data.get('numFound', 0) > 0:
                author_doc = data['docs'][0]
                return {
                    'name': author_doc.get('name', ''),
                    'birth_date': author_doc.get('birth_date', ''),
                    'death_date': author_doc.get('death_date', ''),
                    'top_work': author_doc.get('top_work', ''),
                    'work_count': author_doc.get('work_count', 0)
                }
            return None
        except Exception as e:
            print(f"Error fetching author info: {e}")
            return None

    def get_related_books(self, book_title: str, author: str = None) -> List[Dict]:
        """Get related/recommended books"""
        query = book_title
        if author:
            query = f"{book_title} {author}"
        
        # Search for similar books
        results = self.search_google_books(query, max_results=5)
        # Remove the exact match
        related = [b for b in results if b.get('title', '').lower() != book_title.lower()]
        return related[:4]  # Return top 4 related books

    def fetch_book_data(self, isbn: str) -> Optional[Dict]:
        """Try to fetch book data from multiple sources"""
        # Try Google Books first
        book_data = self.get_book_by_isbn(isbn)
        if book_data and book_data.get('title'):
            return book_data
        
        # Try Open Library as fallback
        book_data = self.get_book_by_isbn_open_library(isbn)
        return book_data

