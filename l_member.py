

# Library Member
# 1.  View My Profile
# 2.  Update Profile Information
# 3.  View Current Loans
# 3.  Search Books


from loan import Loan, load_loans, calculate_overdue_fee
from datetime import datetime


class LibraryMember:
    def __init__(self, member_id, name, gender, city, phone_no):
        self.id = member_id
        self.name = name
        self.gender = gender
        self.city = city
        self.phone_no = phone_no


def load_members():
    members = []
    try:
        with open(r'C:\Users\0216c\OneDrive\Desktop\APU\Python\Library System\library\members.txt', 'r') as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 5:
                    id, name, gender, city, phone_no = data
                    members.append(LibraryMember(int(id), name, gender, city, phone_no))
    except FileNotFoundError:
        print("Members file not found.......")
    return members


def load_loans():
    loans = []
    try:
        with open(r'C:\Users\0216c\OneDrive\Desktop\APU\Python\Library System\library\loans.txt', 'r') as file:
            for line in file:  # loops through each line
                data = line.strip().split(",")
                if len(data) >= 4:  # Minimum 4 values (return_date might be empty)
                    member_name, book_id, loan_date, due_date = data[:4]
                    return_date = data[4] if len(data) > 4 and data[4] else None  # Assign None if return_date is empty

                    loans.append(Loan(
                        member_name,
                        book_id,
                        loan_date,
                        due_date,
                        return_date
                    ))

    except FileNotFoundError:
        print("Loans file not found......")
    return loans


def member_login():
    members = load_members()
    print("\n=== Login ===")

    while True:
        try:
            member_name = input("*Press ENTER back to Main Page \n Enter your name to Login: ").upper()
            if member_name == '':
                break

            # Check if member exists
            member = next((m for m in members if m.name == member_name), None)

            if member:
                print(f"\n--- Welcome, {member.name}! ---")
                return member
            else:
                print("\nMember not found. Please try again......\n")
        except ValueError:
            print("\nInvalid input. Please enter a number......\n")


def view_profile(member):
    print("\n<My Profile>")
    print(f"Member ID: M{member.id}")
    print(f"Name: {member.name}")
    print(f"Gender: {member.gender}")
    print(f"City: {member.city}")
    print(f"Phone No: {member.phone_no}")



def update_profile(member):
    print("\n<Update Profile>")
    print("*Press Enter to keep current value\n")

    # Get new values, keep old ones if empty
    member.name = input(f"Update Name (current: {member.name}): ").upper() or member.name
    member.gender = input(f"Update Gender (M/F) (current: {member.gender}): ").upper() or member.gender
    member.city = input(f"Update City (current: {member.city}): ").upper() or member.city
    member.phone_no = input(f"Update Phone No (current: {member.phone_no}): ") or member.phone_no

    # Save all members with updated information
    members = load_members()
    for m in members:
        if m.id == member.id:
            m.name = member.name
            m.gender = member.gender
            m.city = member.city
            m.phone_no = member.phone_no

    with open(r"C:\Users\0216c\OneDrive\Desktop\APU\Python\Library System\library\members.txt", "w") as file:
        for m in members:
            file.write(f"{m.id},{m.name},{m.gender},{m.city},{m.phone_no}\n")

    print("\n< Profile updated successfully! >")



def search_books():
    print("\n<Search Books>")
    from book import load_books, search_book
    books = load_books()  # Make sure books is loaded before passing
    search_book(books)



def view_loans(name):
    print("\n<My Current Loans>")

    loans = load_loans()
    current_date = datetime.now()
    has_loans = False

    # Load books for reference
    books = []
    try:
        with open(r'C:\Users\0216c\OneDrive\Desktop\APU\Python\Library System\library\catalogue.txt', 'r') as file:
            for line in file:
                books.append(line.strip().split(','))
    except FileNotFoundError:
        print("Catalogue file not found......")
        return

    for loan in loans:
        if loan.member_name == name and (loan.return_date is None or loan.return_date == ""):  # Check for active loans
            has_loans = True
            book_data = next((b for b in books if b[0] == loan.book_id), None)

            if book_data:
                try:
                    # Add proper formatting for single digit months
                    due_date = datetime.strptime(loan.due_date, '%Y-%m-%d')
                    days_overdue = (current_date - due_date).days

                    print(f'Book ID: B{book_data[0]}')
                    print(f'Title: {book_data[1]}')
                    print(f'Author: {book_data[2]}')
                    print(f'Due Date: {loan.due_date}')

                    if days_overdue > 0:
                        fee = calculate_overdue_fee(days_overdue)
                        print(f'Status: OVERDUE by {days_overdue} days')
                        print(f'Overdue Fee: RM{fee:.2f}\n')
                    else:
                        print('Status: On Loan')
                        print('Overdue Fee: RM0.00\n')

                except ValueError:
                    print(f'Book ID: B{book_data[0]}')
                    print(f'Title: {book_data[1]}')
                    print(f'Author: {book_data[2]}')
                    print(f'Due Date: {loan.due_date}')
                    print('Status: Error calculating overdue status\n')
            else:
                print(f'Book with ID B{loan.book_id} not found in catalogue.\n')
    if not has_loans:
        print("You have no books currently on loan.")



def member_menu(member):
    while True:
        print("\n=== Library Member Menu ===")
        print("1. View My Profile")
        print("2. Update Profile Information")
        print("3. View Current Loans")
        print("4. Search Books")
        print("5. Logout")

        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            view_profile(member)

        elif choice == '2':
            update_profile(member)

        elif choice == '3':
            # print("\n<My Current Loans>")
            view_loans(member.name)

        elif choice == '4':
            search_books()

        elif choice == '5':
            print(f"\nGoodbye {member.name}! Logging out......\n")
            break
        else:
            print("\nInvalid choice. Please try again.\n")


def main():
    while True:
        member = member_login()
        if member:
            member_menu(member)
        else:
            print("\n--- Goodbye! ---")
            break



if __name__ == '__main__':
    main()