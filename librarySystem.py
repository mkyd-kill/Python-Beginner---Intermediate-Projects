# library management system in OOP
import sys

class Library:
    def __init__(self):
        """ Display all the available books
            """
        self.availableBooks = []

    def booksAvailable(self):
        for book in self.availableBooks:
            if book in self.availableBooks:
                print("Available Books are: \n")
                print(book)
            else:
                print("There are no books available")

    def addBook(self, book):
        for book in self.availableBooks:
            if book not in self.availableBooks:
                self.availableBooks.append(book)
        return self.availableBooks

    def removeBook(self, book):
        for book in self.availableBooks:
            if book in self.availableBooks:
                self.availableBooks.remove(book)
        return self.availableBooks

    def checkStatus(self):
        """ Checks the issue status of the student
            either lost, paid or lend
        """
        pass

class Student:
    def __init__(self):
        """ Borrow book
            Return book
            Pay for lost book
        """
        def borrowBook(self, item):
            pass

        def returnBook(self):
            pass

        def payBook(self):
            pass

if __name__ == "__main__":
    library = Library()
    library.booksAvailable()
    print(library)