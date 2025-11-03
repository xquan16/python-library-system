
import book
import book_loan

from librarian_info import load_librarians

# track the current logged-in user
current_user = None

def login():   # login function to authenticate users.
    global current_user  # use the global variable to track logged-in user

    staff = load_librarians()   

    print("\n=== Login ===")
    name = input("Enter Username: ").upper()
    id = input("Enter Staff ID: S")

    for librarians in staff:
        if librarians[1] == name and librarians[0] == int(id):  
            current_user = name
            print(f"\n--- Welcome, {current_user}! You are now logged in. ---\n")
            return True
        
    print("\nInvalid username or password. Back to main page.......\n")
    return False  



def logout():  # logout function to reset the current user and exit.
    global current_user  

    if current_user:
        print(f"\n--- {current_user} has logged out. ---")
        current_user = None  
    print("Exiting the login system......")
    return


def main():

    # Login first, if login fails, stop the program
    if not login():
        return  # stop execution if login fails

    while True:
        print("1. Book Management System")
        print("2. Loan Management System")
        print("3. Log Out")

        choice = input("\nEnter your choice (1-3): ")

        if choice == '1':
            book.main()

        elif choice == '2':
            book_loan.main()

        elif choice == '3':
            logout()
            print("\n--- Thank you for using the Library System. Goodbye! ---\n")
            break

        else:
            print("\nInvalid choice. Please try again......\n")


if __name__ == '__main__':
    main()




