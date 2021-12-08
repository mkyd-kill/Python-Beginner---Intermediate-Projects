# library management system in OOP
import sys

class Library:
    def __init__(self):
        """ Display all the available books
            """
        self.availableBooks = {
            1: "The Last Battle",
            2: "The Great Divorce",
            3: "The Last Duel",
            4: "The Screwtape Letters",
            5: "Traceback Cherry",
            6: "Red Notice",
            7: "Chess Set Defined"
            }
        self.inventory = []

    def booksAvailable(self):
        print("Available Books are: \n")
        for number, book in self.availableBooks.items():
            if book in self.availableBooks.values():
                print(book)
            else:
                print("There are no books available")
                break
        return self.availableBooks

    def addBook(self, book):
        for item in self.availableBooks.keys():
            if book not in self.availableBooks.values():
                self.availableBooks[item] = book
        return self.availableBooks

    def removeBook(self, book):
        if book in self.availableBooks.values():
            del self.availableBooks[book]
        else:
            print(f"The Requested Book {book} is Unavailable")
        return self.availableBooks

class Student(Library):
    def borrowBook(self, item):
        for book in self.booksAvailable():
            if item == book:
                self.inventory.append(item)
                self.removeBook(item)
        return self.inventory

    def returnBook(self, item):
        for book in self.booksAvailable():
            if book == item:
                self.inventory.pop(item)
                self.addBook(item)
        return self.inventory

    def checkInventory(self):
        print("Your Book Inventory List:\n")
        for book in self.inventory:
            if book in self.inventory:
                print(book)
            else:
                print("You have borrowed books.")
                break

if __name__ == "__main__": 
    library = Library()
    student = Student()
    run = True
    print("""======LIBRARY MENU=======
        1.Display all available books
        2.Request a book
        3.Return a book
        4.Check my book inventory
        5.exit
        """)
    while run:
        choice = int(input("\nEnter Choice\n:> "))
        try:
            if choice == 1:
                library.booksAvailable()
            elif choice == 2:
                book = str(input("\nEnter the Book Title\n:> "))
                student.borrowBook(book)
            elif choice == 3:
                book = str(input("\nEnter Title of Book wished to be returned\n:> "))
                student.returnBook(book)
            elif choice == 4:
                student.checkInventory()
            elif choice == 5:
                print("\nThank You for using Rom\'s Library. Exiting...")
                run = False
                sys.exit()
        except Exception as e:
            print("\nInvalid Input. Exiting...")
            print(e)
            run = False
            sys.exit()