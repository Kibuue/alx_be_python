class Book:
    """
    Base class representing a book with title and author.
    """
    
    def __init__(self, title, author):
        """
        Initialize book attributes.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author

class EBook(Book):
    """
    Derived class representing an electronic book, inherits from Book.
    """
    
    def __init__(self, title, author, file_size):
        """
        Initialize eBook attributes.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            file_size (int): The file size in KB
        """
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    """
    Derived class representing a printed book, inherits from Book.
    """
    
    def __init__(self, title, author, page_count):
        """
        Initialize print book attributes.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            page_count (int): The number of pages
        """
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    """
    Library class demonstrating composition by managing a collection of books.
    """
    
    def __init__(self):
        """
        Initialize library with an empty list of books.
        """
        self.books = []
    
    def add_book(self, book):
        """
        Add a book to the library.
        
        Args:
            book: Instance of Book, EBook, or PrintBook
        """
        self.books.append(book)
    
    def list_books(self):
        """
        Print details of all books in the library.
        """
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")