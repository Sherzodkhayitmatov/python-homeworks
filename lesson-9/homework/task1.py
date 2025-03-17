class BookNotFoundException(Exception): pass
class BookAlreadyBorrowedException(Exception): pass
class MemberLimitExceededException(Exception): pass

class Book:
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
        
    def borrow(self, book):
        if len(self.borrowed_books) >=3:
            raise MemberLimitExceededException("Limit reached")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException("Book already borrowed")
        book.is_borrowed = True
        self.borrowed_books.append(book)
        
        def return_book(self, book):
            if book in self.borrowed_books:
                book.is_borrowed = False
                self.borrowed_books.remove(book)
                
class Library:
    
    
    def __init__(self):
       self.book = {}
       self.members = {}
    def add_book(self, title):
        self.books[title] = Book[title]
        
    def add_member(self, name):
        self.members[name] = Member[name]
        
    def borrow_book(self, member_name, book_title):
        if book_title not in self.books:
            raise BookNotFoundException("Book is not here")
        self.members[member_name].return_book(self.books[book_title])
        
library = Library()
library.add_book("Harry Poter")
library.add_member("Alice")
                