""" Question 4: Library Management System with Exception Handling 
Scenario: 
A library maintains a catalog of books, allowing users to borrow and return books. Each book 
has a title, author, and availability status. If a user tries to borrow a book that is already 
borrowed, the system should raise an exception. 
Task: 
Create a Book class with attributes: 
• title (str), author (str), and available (bool, default True). 
Create a Library class with: 
• Attributes: A list of books. 
• Methods:  
o add_book(book): Adds a book to the catalog. 
o borrow_book(title): Changes the book’s availability to False if available; 
otherwise, raises a BookNotAvailableException. 
o return_book(title): Marks the book as available if found in the catalog. 
Define a custom exception BookNotAvailableException for handling book unavailability. 
Steps to Solve: 
1. Create a Book class with the required attributes. 
2. Define a Library class that manages books. 
3. Implement add_book(book), borrow_book(title), and return_book(title). 
4. Define a custom exception BookNotAvailableException. 
5. Write a test case where a user tries to borrow an already borrowed book, and handle 
the exception. 
Example: 
library.add_book("Python Programming") 
library.add_book("Data Science Handbook") 
library.borrow_book("Python Programming") # Borrow an available book 
library.borrow_book("Python Programming") # Attempt to borrow the same book again 
library.display_books() # Display available books after borrowing 
Output: 
Book 'Python Programming' has been borrowed. 
Error: Book 'Python Programming' is not available in the library. 
Available books: - Data Science Handbook """

# Step 1: Define a custom exception for unavailable books
class BookNotAvailableException(Exception):
    def __init__(self, message="The requested book is not available."):
        super().__init__(message)

# Step 2: Create a Book class
class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

# Step 3: Define a Library class to manage books
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = False
                    print(f"Book '{title}' has been borrowed.")
                    return
                else:
                    raise BookNotAvailableException(f"Book '{title}' is not available in the library.")
        print(f"Book '{title}' not found in the catalog.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                print(f"Book '{title}' has been returned.")
                return
        print(f"Book '{title}' not found in the catalog.")

    def display_books(self):
        available_books = [book.title for book in self.books if book.available]
        if available_books:
            print("Available books:", ", ".join(available_books))
        else:
            print("No books available.")

# Step 4: Testing the Library System
library = Library()

# Adding books to the library
library.add_book(Book("Python Programming", "John Doe"))
library.add_book(Book("Data Science Handbook", "Jane Smith"))

# Borrowing books
try:
    library.borrow_book("Python Programming")  # Borrowing an available book
    library.borrow_book("Python Programming")  # Attempting to borrow again (should raise exception)
except BookNotAvailableException as e:
    print(f"Error: {e}")

# Display available books after borrowing
library.display_books()
