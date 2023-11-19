from models import session, Book
import sys
sys.path.append('/home/raj/Desktop/Distributed_system/Microservices/Book Inventory system/Inventory_models/external_operations.py')
from external_operations import publish_book


def add_book(title, author, isbn, genre, quantity):
    if existing_book := session.query(Book).filter_by(isbn=isbn).first():
        return f"Book with ISBN {isbn} already exists: {existing_book.title} by {existing_book.author}."
    new_book = Book(title=title, author=author, isbn=isbn, genre=genre, quantity=quantity)
    session.add(new_book)
    session.commit()
    return f"New book added: {title} by {author} with ISBN {isbn} and sold {quantity}."


def delete_book(isbn_or_id):
    try:
        book_id = int(isbn_or_id)
        book = session.query(Book).filter_by(id=book_id).first()
    except ValueError:
        book = session.query(Book).filter_by(isbn=isbn_or_id).first()

    if book:
        session.delete(book)
        session.commit()
        return f"Book with ISBN/ID {isbn_or_id} deleted successfully."
    else:
        return f"Book with ISBN/ID {isbn_or_id} not found. Deletion failed."


def modify_book(isbn_or_id, title=None, author=None, genre=None, quantity=None):
    try:
        book_id = int(isbn_or_id)
        book = session.query(Book).filter_by(id=book_id).first()
    except ValueError:
        book = session.query(Book).filter_by(isbn=isbn_or_id).first()

    if book:
        if title is not None:
            book.title = title
        if author is not None:
            book.author = author
        if genre is not None:
            book.genre = genre
        if quantity is not None:
            book.quantity = quantity

        session.commit()
        return f"Book with ISBN/ID {isbn_or_id} modified successfully."
    else:
        return f"Book with ISBN/ID {isbn_or_id} not found. Modification failed."

def retrieve_books(criteria, value):
    criteria_mapping = {
        'isbn': Book.isbn,
        'title': Book.title,
        'author': Book.author,
        'genre': Book.genre,
    }

    if criteria not in criteria_mapping:
        return "Invalid criteria. Valid criteria are: isbn, title, author, genre."

    books = session.query(Book).filter(criteria_mapping[criteria].ilike(f'%{value}%')).all()

    return [
        {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'isbn': book.isbn,
            'genre': book.genre,
            'quantity': book.quantity,
        }
        for book in books
    ]

# book_operations.py
def add_book_and_publish(title, author, isbn, genre, quantity):
    book_id = add_book(title, author, isbn, genre, quantity)
    result = publish_book(book_id)

    return f"Book with ID {book_id} added and published successfully. Result: {result}"

def add_book(title, author, isbn, genre, quantity):
    # Logic to add a book to the database
    pass
