class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' by {book.author} ({book.copies} copies)")

    
    def return_book(self, book):
        book.copies += 1
        print(f"Returned '{book.title}'. Copies available now: {book.copies}")




    def list_books(self):
        if not self.books:
            print("No books in the library yet.")
        else:
            print("\nLibrary Collection:")
            for book in self.books:
                print(f"- {book.title} by {book.author} ({book.copies} copies)")


# Testing it
book1 = Book("The Alchemist", "Paulo Coelho", 3)
book2 = Book("Things Fall Apart", "Chinua Achebe", 5)

library = Library()
library.add_book(book1)
library.add_book(book2)
library.list_books()


library.return_book(book1)

library.list_books()


        

 