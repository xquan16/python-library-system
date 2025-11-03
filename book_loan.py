from datetime import datetime, timedelta

from book import load_books, save_books
from member_info import load_members



def load_loans():
    loans = []
    try:
        with open(r'C:\chris\APU\Y1 Sem1\Python\Library System Code\loans.txt', 'r') as file:  #loan.txt
            for line in file:
                data = line.strip().split(",") # strip(): remove whitespace / split(): split data by comma
                if len(data) >= 4:
                    loans.append({
                        'member_name': data[0],
                        'book_id': int(data[1]),
                        'loan_date': data[2],
                        'due_date': data[3],
                        'return_date': data[4] if len(data) > 4 and data[4] else None
                    })
    except FileNotFoundError:
        print("Loans file not found......")
    return loans



def save_loans(loans):
    with open(r'C:\Users\0216c\OneDrive\Desktop\APU\Python\Library System\library\loans.txt', 'w') as file:
        for loan in loans:
            return_date = loan['return_date'] if loan['return_date'] else ""
            file.write(f"{loan['member_name']},{loan['book_id']},{loan['loan_date']},"
                      f"{loan['due_date']},{return_date}\n")



def calculate_overdue(due_date):
    days_overdue = (datetime.now() - datetime.strptime(due_date, '%Y-%m-%d')).days  # strptime = string prase time (convert string to datetime)
    if days_overdue <= 0:                                                           # .days = extracts the difference between days as an integer
        return 0, 0
    fees = {1: 2.00, 2: 3.00, 3: 4.00, 4: 5.00, 5: 6.00}
    return days_overdue, fees.get(days_overdue, 10.00)  #.get = set default fee is 10.00


 
def get_member_loans(member_name):  # use for process_loan()  &  process_return
    active_loans = []  # create to store the member's current loans
    total_fee = 0
    
    for loan in load_loans():
        if loan['member_name'] == member_name and not loan['return_date']:  # check loan which match member, if matched mean return_date None 

            days_overdue, fees = calculate_overdue(loan['due_date']) # call calculate_overdue() function
            active_loans.append({
                'book_id': loan['book_id'],
                'loan_date': loan['loan_date'],
                'due_date': loan['due_date'],
                'days_overdue': days_overdue,
                'fee': fees
            })
            total_fee += fees    
            
    return active_loans, total_fee




def view_all_loans():  # 1.
    loans = load_loans()
    print("\n<All Loans>")
    print(f"[Loaded {len(loans)} loans\n]")
    active = False
    books = load_books()  # call load books() function to show titles (import book.py)
    
    for loan in load_loans():
        if not loan['return_date']:
            active = True
            days_overdue, fees = calculate_overdue(loan['due_date'])  # call calculate_overdue() function
            status = f"| Overdue {days_overdue} days, Fee: RM{fees:.2f}" if days_overdue > 0 else "Active"
            
            for book in books:
                if book['id'] == loan['book_id']:  # find match book id in [loans] and [books]
                    book_title = book['title']  # extract book title
                    author = book['author']  # extract book author
                    break
                    
            print(f"| Member: {loan['member_name']}")
            print(f"| Book ID: (B{loan['book_id']}) - {book_title}, By {author}")  
            print(f"| Loan Date: {loan['loan_date']}")
            print(f"| Due Date: {loan['due_date']}")
            print(f"| Status: {status}\n")
    
    if not active:
        print("No active loans found......")





def process_loan():  # 2.
    print("\n<Process New Loan>")
    
# checking member exists
    member = input("Enter Member Name: ").upper()

    members = load_members()  # call load member() function to checking member exists (import member_info.py)
    member_exists = False
    for m in members:
        if m['name'] == member:  # if the member name in members list == input name
            member_exists = True
            break
    
    if not member_exists:
        print("Member not found......")
        return
        
    active_loans, total_fee = get_member_loans(member)   # call get_member_loans(member) to check member loan status
    
    print(f"\nActive loans for {member}: {len(active_loans)}")  # show have how many loan

    if total_fee > 0:
        print(f"| Cannot process loan: Outstanding fees RM{total_fee:.2f} |")   # if member have overdue book
        return
    
    if len(active_loans) >= 5:    # member can only borrow up to 5 book
        print("| Cannot process loan: Maximum limit (5 books) reached |")
        return
        
    try:          
# check if book exists and is available
        book_id = int(input("\n*Enter Book ID to borrow: B"))

        books = load_books()   # call load books() function (import book.py)
        book_found = False     # track book exists
        book_for_loan = False  # track book available for loan

        for book in books:
            if book['id'] == book_id:  # check the loan of the user input book id and books list 
                book_found = True
                if book['available']:
                    book_for_loan = True  # book available to borrow
                    book['available'] = False  # update availability, book 'OnLoan', cause process new loan
                break
        
        if not book_found:
            print(f"\n| Book B{book_id} not found...... |")
            return
        if not book_for_loan:  
            print(f"\n| Book B{book_id} is currently On Loan |")
            return

    # save member name and book id into loans list, loan_date/due_date auto generate by system        
        loans = load_loans()  # call load_loans() function
        loans.append({
            'member_name': member,
            'book_id': book_id,
            'loan_date': datetime.now().strftime('%Y-%m-%d'),
            'due_date': (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d'),
            'return_date': None
        })
        
        save_loans(loans)
        save_books(books)  # save updated book availability
        print(f"\n~~~ Loan processed successfully for {member} ~~~")
        print(f"| (B{book_id}), {book['title']}, By {book['author']} -- Due date: {loans[-1]['due_date']}  |")        
    except ValueError:
        print("\nInvalid Book ID format......")



def process_return():  # 3.
    print("\n<Process Book Return>")
    member = input("Enter Member Name: ").upper()
    
# checking member exists.
    members = load_members()
    member_exists = False
    for m in members:
        if m['name'] == member:
            member_exists = True
            break
    
    if not member_exists:
        print("Member not found......")
        return
            
# check active loan
    active_loans, total_fee = get_member_loans(member)   # call get_member_loans(member) to check member loan status
    
    if not active_loans:
        print(f"No active loans found for {member}")
        return

    # display active loan info
    books = load_books()
    print(f"\nActive loans for {member}: {len(active_loans)}")  # show have how many loan
    for loan in active_loans:
        status = "Overdue" if loan['days_overdue'] > 0 else "Active"

        title = "Unknown"
        author = "Unknown"
        for book in books:  # find and show book title and author
            if book['id'] == loan['book_id']:
                title = book['title']
                author = book['author']
                break
                
        print(f"\n| Book: (B{loan['book_id']}), {title}, By {author}")
        print(f"| Loan Date: {loan['loan_date']}")
        print(f"| Due Date: {loan['due_date']}")
        print(f"| Status: {status}")
        if loan['fee'] > 0:
            print(f"| Overdue Fee: RM{loan['fee']:.2f}")
    
    if total_fee > 0:
        print(f"\n===Total overdue fees: RM{total_fee:.2f}===")
    
# process book return
    try:
        book_id = int(input("\nEnter Book ID to return: B"))
        loans = load_loans()
        books = load_books()  # load books to update availability
        
        for loan in loans:
            if (loan['member_name'] == member and 
                loan['book_id'] == book_id and 
                not loan['return_date']):
                loan['return_date'] = datetime.now().strftime('%Y-%m-%d')
                
                # update book availability
                for book in books:
                    if book['id'] == book_id:
                        book['available'] = True  # available to borrow, cause already returned
                        break
                        
                save_loans(loans)
                save_books(books)  # save updated book availability
                print(f"\n~~~ Book returned successfully ~~~")
                print(f"| (B{book_id}), {book['title']}, By {book['author']} |")    
                return
        print(f"\n| No active loan found for Book ID B{book_id} |")
    except ValueError:
        print("Invalid Book ID format......")



def main():
    while True:
        print("\n--- Loan Management System ---")
        print("1. View All Loans")
        print("2. Process New Loan")
        print("3. Process Book Return")
        print("4. Back")

        choice = input("\nEnter your choice (1-4): ")
        if choice == '1':
            view_all_loans()

        elif choice == '2':
            process_loan()

        elif choice == '3':
            process_return()

        elif choice == '4':
            break

        else:
            print("\nInvalid choice. Please try again......")


if __name__ == '__main__':
    main()
    