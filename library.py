class Library():
    def __init__(self, list):
        self.books_list = list
        self.available_books_list = list[:]
        self.books_lent = {}  # key-book value-user name

    def display_available_books(self):
        for book in self.available_books_list:
            print(book)

    def display_all_books(self):
        for book in self.books_list:
            print(book)

    def lend_book(self, name, book):
        if book not in self.books_list:
            print("Incorrect book name. Please check book list")
            return
        if book in self.available_books_list:
            self.books_lent.update({book: name})
            self.available_books_list.remove(book)
            print("You can take the book..")
        else:
            print("The book is already taken by " + self.books_lent[book])

    def return_book(self, book):
        del self.books_lent[book]
        self.available_books_list.append(book)


if __name__ == "__main__":
    lib = Library(["The Life Divine", "Da Vinci Code", "The Alchemist", "Educated", "Harry Potter"])
    print("Welcome to Library. Enter an option. ")
    while True:
        print("1.Display available books")
        print("2.Display all books ")
        print("3.Borrow a book")
        print("4.Return a book")
        print("5.Quit")
        user_choice = int(input())
        if user_choice == 1:
            lib.display_available_books()
        elif user_choice == 2:
            lib.display_all_books()
        elif user_choice == 3:
            name = input("Enter User Name ")
            book = input("Enter Book Name")
            lib.lend_book(name, book)
        elif user_choice == 4:
            book = input("Enter the name of the book")
            lib.return_book(book)
        elif user_choice == 5:
            break
        else:
            print("Invalid choice")
