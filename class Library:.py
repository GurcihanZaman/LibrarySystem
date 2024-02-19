class Library:
    def __init__(self, books):
        self.books = books
        self.file = open(self.books, "a+")


    def __del__(self):
        self.file.close()


         


    def list_books(self):
        self.file.seek(0)
        
        lines = self.file.readlines()
        print("List of Books")
        for line in lines:
            book_information = line.strip().split(',')
            if len(book_information) >= 2:
                book_name = book_information[0].strip()
                author = book_information[1].strip()
                print(f"Book Name: {book_name}, Author: {author}")
            else:
                print("Invalid book entry:", line.strip())


    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the author of the book: ")
        year = input("Enter the publication year: ")
        page = input("Enter number of pages the book: ")
        all_info = f"{title}, {author}, {year}, {page}\n"

        self.file.seek(0)
        lines = self.file.readlines()
        for line in lines:
               if title in line:
                  print(f"The library already has the book '{title}'.")
                  return
        self.file.write(all_info)
        print(f"Book '{title}' added to the library.")

    def remove_book(self):
        lines = self.file.readlines()
        self.file.seek(0)
        #self.book_title = book_title
        book_title = input("Enter the book title that you want to remove: ")
        
        new_lines = []
        book_in = False
        for line in lines:
            if book_title not in line:
                new_lines.append(line)

            else:
                book_in = True
        self.file.truncate(0)  
        self.file.seek(0)  
        for line in new_lines:
            self.file.write(line)

        self.file.flush()
        if book_in:
           print(f"Book '{book_title}' removed from the library.")

        else:
            print(f"Library has no such a book called '{book_title}'.")    



def print_menu():
    print("*** MENU ***")
    print("1. List Books")
    print("2. Add Book")
    print("3. Remove Book")
    print("4. Quit")


lib = Library("Books")
while True:
    print_menu()
    choice = input("Please choose one of the processes: ")
    if choice == "1":

        lib.list_books()

    elif choice == "2":
        lib.add_book()

    elif choice == "3":
        #removing_book = input("Enter the title of the book to remove: ")
        lib.remove_book()

    elif choice == "4":
        break
    else:
        print("Invalid choice. Please enter a valid option.")            

    






        
        
