from books_operations import add_book, delete_book, modify_book, retrieve_books

def main():
    while True:
        print("\nMenu:")
        print("1. Add a book")
        print("2. Delete a book")
        print("3. Modify a book")
        print("4. Retrieve books")
        print("5. Exit")

        choice = input("Enter your choice (1, 2, 3, 4, or 5): ")

        if choice == '1':

            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            isbn = input("Enter the ISBN: ")
            genre = input("Enter the genre: ")
            quantity = int(input("Enter the quantity: "))
            result = add_book(title, author, isbn, genre, quantity)
            print(result)

        elif choice == '2':
           
            isbn_or_id = input("Enter the ISBN or ID of the book to delete: ")
            result = delete_book(isbn_or_id)
            print(result)

        elif choice == '3':
    
            isbn_or_id = input("Enter the ISBN or ID of the book to modify: ")
            title = input("Enter the new book title (press Enter to keep current): ")
            author = input("Enter the new author (press Enter to keep current): ")
            genre = input("Enter the new genre (press Enter to keep current): ")
            quantity = input("Enter the new quantity (press Enter to keep current): ")

            quantity = int(quantity) if quantity.strip() else None

            result = modify_book(isbn_or_id, title=title, author=author, genre=genre, quantity=quantity)
            print(result)

        elif choice == '4':
            criteria = input("Enter the criteria to retrieve books (isbn, title, author, genre): ")
            value = input(f"Enter the {criteria} to search for: ")
            result = retrieve_books(criteria, value)
            print(result)

        elif choice == '5':

            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
