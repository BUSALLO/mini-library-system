

def create_file():
    try:
        file = open("books.txt", "x")
        file.close()
        print("File created successfully!")
    except FileExistsError:
        print("File already exists.")



def write_file():
    file = open("books.txt", "w")  # overwrite mode

    book = input("Enter book title: ")
    file.write(book + "\n")

    file.close()
    print("Book saved!")
    
    
    
    
    
    
def add_book():
    file = open("books.txt", "a")  # append mode

    book = input("Enter new book: ")
    file.write(book + "\n")

    file.close()
    print("Book added!")
    
    
    
    
def view_books():
    try:
        file = open("books.txt", "r")
    except FileNotFoundError:
        print("No books file found. Create it first with option 1.")
        return

    lines = file.readlines()
    file.close()

    if not lines:
        print("\nBooks in library: no books found.")
        return

    print("\nBooks in library:")
    for i, book in enumerate(lines):
        print(i, book.strip())


def update_book():
    file = open("books.txt", "r")
    books = file.readlines()
    file.close()

    view_books()  # show list first

    index = int(input("Enter index to update: "))
    new_book = input("Enter new book name: ")

    books[index] = new_book + "\n"

    file = open("books.txt", "w")
    file.writelines(books)
    file.close()

    print("Book updated!")
    
    
def delete_book():
    file = open("books.txt", "r")
    books = file.readlines()
    file.close()

    view_books()  # show list first

    index = int(input("Enter index to delete: "))

    books.pop(index)

    file = open("books.txt", "w")
    file.writelines(books)
    file.close()

    print("Book deleted!")
    
def search_book():
    name = input("Enter book to search: ")

    file = open("books.txt", "r")

    found = False
    for line in file:
        if name.lower() in line.lower():
            print("Found:", line.strip())
            found = True

    file.close()

    if not found:
        print("Book not found.")
    
while True:
    print("\n--- MINI LIBRARY SYSTEM ---")
    print("1. Create File")
    print("2. Write File")
    print("3. Add Book")
    print("4. View Books")
    print("r. Read Books")
    print("5. Update Book")
    print("6. Delete Book")
    print("7. Search Book")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_file()
    elif choice == "2":
        write_file()
    elif choice == "3":
        add_book()
    elif choice == "4":
        view_books()
    elif choice.lower() == "r":
        view_books()
    elif choice == "5":
        update_book()
    elif choice == "6":
        delete_book()
    elif choice == "7":
        search_book()
    elif choice == "8":
        break
    else:
        print("Invalid choice")