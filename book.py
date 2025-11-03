
def load_books():  # to load books from txt file and return to list / to preserve data
    books = []  # create a list to store book

    try:
        with open(r"C:\chris\APU\Y1 Sem1\Python\Library System Code\catalogue.txt", "r") as file:  # read file

            for line in file:
                data = line.strip().split(",")  # strip(): remove whitespace / split(): split data by comma (1,ABC,BRYAN --> '1','ABC','BRYAN')
                if len(data) >= 4:  # (id, title, author, availability)
                    id, title, author, availability = data[:4]  # extract first 4 element
                    available = (availability == 'Available')  # become boolean
                    book = {'id': int(id), 
                            'title': title, 
                            'author': author, 
                            'available': available
                            }  # create dictionary for book.
                    books.append(book)  # add book dictionary to list
    except FileNotFoundError:
        print("Catalogue file not found......") # if file not found or cannot open
    return books



def save_books(books): 
    with open(r"C:\Users\0216c\OneDrive\Desktop\APU\Python\Library System\library\catalogue.txt", "w") as file:
        for book in books:
            availability = 'Available' if book['available'] else 'On Loan' # convert boolean to string True='Available' / False='On Loan'
            file.write(f"{book['id']},{book['title']},{book['author']},{availability}\n") # write to the file



def display_books(books): # 1.
    if not books:
        print("No books in the library.")
    else:
        for book in books:
            availability = 'Available' if book['available'] else 'On Loan'
            print(f"(ID: B{book['id']}), {book['title']}, By {book['author']}, {availability}")



def add_book(books): # 2.
    try:
        id = int(input("Enter book ID: B"))
        title = input("Enter book title: ").upper()
        author = input("Enter book author: ").upper()
        book = {'id': id, 'title': title, 'author': author, 'available': True}
        books.append(book)
        save_books(books)
        print("\n< Book added successfully! >")
    except:
        print("\nBook added unsuccessfully! Invalid or incomplete information...... >")



def remove_book(books): # 3.
    id = int(input("Enter the ID of the book to remove: B"))
    for book in books:  # loop books list
        if book['id'] == id:  # if find the book id in books list that match with input, romove book
            books.remove(book) 
            save_books(books)
            print("< Book removed successfully. >")
            return
    print("Book not found......") 



def edit_book(books): # 4.
    try:  # aviod input not integer or empty
        id = int(input("Enter the ID of the book to edit: B"))  
    except ValueError:
        print("\nInvalid input! Only integer ID is allowed. Exit......")
        return

    found = False  
    for book in books: # loop books list
        if book["id"] == id:  # find the match id
            found = True  

            print('\n~ Press ENTER to keep current information ~')
            print(f'Current: [ (ID: B{book["id"]}), {book["title"]}, By {book["author"]}, '
                  f'{"Available" if book["available"] else "On Loan"} ]\n')
            
            new_title = input(f"Enter new title (current: {book['title']}): ").upper() or book['title']
            new_author = input(f"Enter new author (current: {book['author']}): ").upper() or book['author']
            book['title'], book['author'] = new_title, new_author
            save_books(books)
            print("\n< Book information updated successfully. >")
            return # exit after updating book
        
    if not found:  # if book id not found
        print('\nBook not found! Exit......')



def search_book(books): # 5. 
    while True:
        print('1. Book ID')
        print('2. Title')
        print('3. Author')
        print('4. Back')

        search = input('\nEnter your choice(1-4) to Search by: ')

        if search == '1':
            try:  # aviod input not integer or empty
                id = int(input("\nEnter Book ID: B"))  
            except ValueError:
                print("\nInvalid input! Only integer ID is allowed. Exit......")
                return

            found = False
            for book in books:
                if book["id"] == id:
                    availability = 'Available' if book['available'] else 'On Loan'
                    print(f'[ (ID: B{book["id"]}), {book["title"]}, By {book["author"]}, {availability} ]\n')
                    found = True
            if not found:
                print("\nBook not found. Please try again......\n")

        elif search == '2':
            title = input("\nEnter Book Title: ").upper()

            found = False
            for book in books:
                if book['title'] == title:
                    availability = 'Available' if book['available'] else 'On Loan'
                    print(f'[ (ID: B{book["id"]}), {book["title"]}, By {book["author"]}, {availability} ]\n')
                    found = True
            if not found:
                print("\nBook not found. Please try again......\n")

        elif search == '3':
            author = input("\nEnter Book Author: ").upper()

            found = False
            for book in books:
                if book['author'] == author:
                    availability = 'Available' if book['available'] else 'On Loan'
                    print(f'[ (ID: B{book["id"]}), {book["title"]}, By {book["author"]}, {availability} ]\n')
                    found = True
            if not found:
                print("\nBook not found. Please try again......\n")

        elif search == '4':
            break

        else:
            print("\nInvalid choice. Please try again......\n")


# 1. Display All Book
# 2. Add New Book
# 3. Remove Book
# 4. Edit Book Information
# 5. Search Book
# 6. Log Out


def main():
    while True:
        books = load_books()

        print("\n--- Books Management System ---")
        print(f'[Loaded {len(books)} books in library.]\n')
        print("1. Display All Books")
        print("2. Add New Book")
        print("3. Remove Book")
        print("4. Edit Book Information")
        print("5. Search Book")
        print("6. Back")

        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            print('\n<Books Catalogue>')
            display_books(books)

        elif choice == '2':
            print('\n<Books Catalogue>')
            display_books(books)
            print('\n<Add New Book>')
            add_book(books)

        elif choice == '3':
            print('\n<Books Catalogue>')
            display_books(books)
            print('\n<Remove Book>')
            remove_book(books)

        elif choice == '4':
            print('\n<Books Catalogue>')
            display_books(books)
            print('\n<Edit Book Information>')
            edit_book(books)

        elif choice == '5':
            print('\n<Search Book>')
            search_book(books)

        elif choice == '6':
            print("\n--- Thank you for using the Library Books Management System. Goodbye! ---\n")
            break

        else:
            print("\nInvalid choice. Please try again......\n")



if __name__ == '__main__':
    main()