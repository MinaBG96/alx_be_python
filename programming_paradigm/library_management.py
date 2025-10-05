class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # خاصية خاصة لتتبع حالة الكتاب

    def check_out(self):
        """Mark the book as checked out (unavailable)."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as available again."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if the book is not checked out."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # قائمة خاصة تحتوي على الكتب الموجودة في المكتبة

    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"'{title}' is not available.")

    def return_book(self, title):
        """Return a book to the library by its title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"'{title}' was not checked out.")

    def list_available_books(self):
        """List all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(f"{book.title} by {book.author}")
