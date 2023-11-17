from models import session, Book


def add_book(title, author, isbn, genre, quantity):
    existing_book = session.query(Book).filter_by(isbn=isbn).first()

    if existing_book:
        response_message = f"Book with ISBN {isbn} already exists: {existing_book.title} by {existing_book.author}."

    else:
        new_book = Book(title=title, author=author, isbn=isbn, genre=genre, quantity=quantity)
        session.add(new_book)
        response_message = f"New book added: {title} by {author} with ISBN {isbn} and selled {quantity}."
        
        session.commit()

    return print(response_message)


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

    formatted_books = []
    for book in books:
        formatted_books.append({
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'isbn': book.isbn,
            'genre': book.genre,
            'quantity': book.quantity,
        })

    return formatted_books
