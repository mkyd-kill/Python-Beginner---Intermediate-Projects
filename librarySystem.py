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
            print(f"[{number}] {book}")

    def removeBook(self, book):
        for num, item in self.availableBooks.items():
            if book == item:
                del self.availableBooks[num]
            else:
                print(f"The Requested Book `{item}` is Unavailable")
                break

class Student(Library):
    def borrowBook(self, book_num):
        for num, item in self.availableBooks.items():
            if book_num == num:
                self.inventory.append(item)

    def returnBook(self, item):
        for num, book in self.availableBooks.items():
            if num == item:
                if book in self.inventory:
                    self.inventory.remove(book)
                else:
                    print("You have no books to return")
                    pass
        return self.inventory

    def checkInventory(self):
        print("Your Book Inventory List:\n")
        for book in self.inventory:
            if book in self.inventory:
                print(book)
            else:
                print("You have no borrowed books.")
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
        choice = int(input("\nEnter Menu Choice\n:> "))
        try:
            if choice == 1:
                library.booksAvailable()
            elif choice == 2:
                book_num = int(input("\nEnter Book Index you wish to Borrow\nExample: 1 for The Last Battle\n:> "))
                student.borrowBook(book_num)
            elif choice == 3:
                book_num = int(input("\nEnter Index of the Book you wish to return\nExample: 1 for The Last Battle\n:> "))
                student.returnBook(book_num)
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