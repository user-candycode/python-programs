import shutil


# Creating library related operations
class Library:

    def __init__(self, list_of_books):
        self.books = list_of_books

    # print available book
    def displayAvailableBooks(self):
        print("Books present in the library are: ")
        for index, book in enumerate(self.books):
            print(str(index+1)+":", book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(
                f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print(
                "Sorry this book has been issued to somebody else. \nPlease wait until the book is returned.")
            return False

    # return a book
    def returnBook(self, bookName):
        self.books.add(bookName)
        print("thanks for returning your book")


class Student:
    def __init__(self) -> None:
        self.bookList = {}

    def requestBook(self):
        self.book = input("Enter the name of the want you want to borrow")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the want you want to return")
        return self.book


# Get the width of the console window
columns, rows = shutil.get_terminal_size()

# Set the character you want to print
char = '='
text = "Welcome to the central library."
padding = " " * ((columns-len(text)) // 2)


if __name__ == "__main__":

    # List hardcoded as the book database

    l = {'Algorithms', 'Django', 'Clrs', 'Python'}

    # Creating object to library
    central_Library = Library(l)
    student = Student()
    # central_Library.displayAvailableBooks()

    # Starting infinite loop
    while (True):
        print(char * columns)
        print(padding+text)
        print(char * columns)
        print('''MENU:
            1. Listing all available books
            2. Request a book
            3. Return a book
            4. To quit the menu and exit program.''')

        user_input = int(input("Enter a input:"))
        print()
        if user_input == 1:
            central_Library.displayAvailableBooks()
        elif user_input == 2:
            central_Library.borrowBook(student.requestBook())
        elif user_input == 3:
            central_Library.returnBook(student.returnBook())
        elif user_input == 4:
            print("Thanks for choosing Central library have a great time ahead.")
            exit()
        else:
            print("Invalid Choice!")
