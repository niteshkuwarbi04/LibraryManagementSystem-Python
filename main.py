'''
Implemented a student library system using OOPs where students can borrow a book from the list of books.
Created a separate Library and Student class. 
I've used constructors
This program is menu driven. 
You are free to choose methods and attributes of your choice to implement this functionality
'''

class Library:

    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("The books present in the library are: ")
        for book in self.books:
            print(" -" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please take it safe and return within 30 days.")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, this book is either not available or it's already been issued to someone else.")  
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print(f"Thanks for returning this book. Have a great day ahead.")

class Student:

    def __init__(self):
        self.bookList =[]

    def requestBook(self,):
        self.book = input("Enter the name of the book you want to borrow: \t")
        return self.book
        
    def returnBook(self,):
        self.book = input("Enter the name of the book you want to add/return: \t")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(["Autobiography of a yogi", "Freedom from the known", "Think on these things", "Karma", "The oath of Vayaputras", "Atlus Shrugged"])
    student = Student()
    # centralLibrary.displayAvailableBooks()

    while(True):
        WelcomMsg = '''\n===== Welcome to the Central Library =====
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(WelcomMsg)

        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a ==2:
            centralLibrary.borrowBook(student.requestBook())
        elif a==3:
            centralLibrary.returnBook(student.returnBook())
        elif a==4:
            print("Thanks for choosing Central Library. Have a good day.")
            exit()
        else:
            print("Invalid choice")
        print()