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
    
    def __str__(self):
        """
        String representation of the Book.
        """
        return f"Book: {self.title} by {self.author}"

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
    
    def __str__(self):
        """
        String representation of the EBook.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

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
    
    def __str__(self):
        """
        String representation of the PrintBook.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

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
            print(book)