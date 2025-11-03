
# loan management file

from datetime import datetime, timedelta


class Loan:
    def __init__(self, member_name, book_id, loan_date, due_date, return_date = None):
        self.member_name = member_name
        self.book_id = book_id
        self.loan_date = loan_date
        self.due_date = due_date
        self.return_date = return_date


def load_loans():
    loans = []
    try:
        with open(r'C:\Users\0216c\OneDrive\Desktop\APU\Python\Library System\library\loans.txt', 'r') as file:
            for line in file:  # loops through each line
                data = line.strip().split(",")
                if len(data) >= 4:  # Minimum 4 values (return_date might be empty)
                    member_name, book_id, loan_date, due_date = data[:4]
                    # if return_date present/not empty, assigns value, else assigns None
                    return_date = data[4] if len(data) > 4 and data[4] else None

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


def save_loans(loans):
    with open(r'C:\Users\0216c\OneDrive\Desktop\APU\Python\Library System\library\loans.txt', 'w') as file:
        for loan in loans:
            return_date = loan.return_date if loan.return_date else ""
            file.write(f"{loan.member_name},{loan.book_id},"
                       f"{loan.loan_date},{loan.due_date},{return_date}\n")


def calculate_overdue_fee(days_overdue):  # Calculate overdue fee based on Table 1
    if days_overdue <= 0:
        return 0.00
    elif days_overdue == 1:
        return 2.00
    elif days_overdue == 2:
        return 3.00
    elif days_overdue == 3:
        return 4.00
    elif days_overdue == 4:
        return 5.00
    elif days_overdue == 5:
        return 6.00
    else:
        return 10.00


def create_loan(member_name, book_id, loans):
    """Create a new loan record"""
    # Set loan dates
    loan_date = datetime.now().strftime('%Y-%m-%d')
    due_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')

    # Create and return new loan
    return Loan(member_name, book_id, loan_date, due_date)


def update_book_status(book_id, status):
    """Update book availability status"""
    try:
        with open(r'C:\Users\0216c\OneDrive\Desktop\APU\Python\Library System\library\catalogue.txt', 'r') as file:
            books = [line.strip() for line in file]
    except FileNotFoundError:
        return False

    with open(r'C:\Users\0216c\OneDrive\Desktop\APU\Python\Library System\library\catalogue.txt', 'w') as file:
        for book in books:
            book_data = book.split(',')
            if int(book_data[0]) == book_id:
                book_data[3] = status
            file.write(','.join(book_data) + '\n')


def check_loan_eligibility(member_name, loans):  # Check if member is eligible for new loan
    active_loans = 0  # Count of active loans by this member
    overdue = False  # Tracks if the member has any overdue loans
    current_date = datetime.now()  # Get the current date and time

    for loan in loans:
        if loan.member_name == member_name and not loan.return_date:
            active_loans += 1    # if loan belong member=member.name and not yet return, add 1 loan
            try:  # avoid system stop run when any date error found (e.g. 2024.20.32)
                due_date = datetime.strptime(loan.due_date, '%Y-%m-%d')  # strptime = str parse to time
            except ValueError:
                print(f"Error parsing date for loan {loan.loan_id}")
                continue  # Skip to the next loan

            # Calculate days overdue
            days_overdue = (current_date - due_date).days

            if days_overdue > 0:
                overdue = True
                fee = calculate_overdue_fee(days_overdue)  # Calculate overdue fee
                print(f"Loan {loan.loan_id} is overdue by {days_overdue} days. Fee: RM{fee:.2f}")

    return active_loans < 5 and not overdue  # Eligible if < 5 active loans and no overdue books


def process_loan(member_name, book_id):
    """Process a new book loan"""
    loans = load_loans()

    # Check eligibility
    if not check_loan_eligibility(member_name, loans):
        print(f"{member_name} is not eligible for a loan.")
        return False, "Member has reached loan limit or has overdue books"

    # Create new loan
    new_loan = create_loan(member_name, book_id, loans)
    loans.append(new_loan)
    save_loans(loans)
    # Update book status
    update_book_status(book_id, "On Loan")

    return True, f"Loan created successfully. Due date: {new_loan.due_date}"


def process_return(member_name, book_id):
    """Process the return of a loaned book."""
    loans = load_loans()

    # Find the loan matching the given member and book ID with no return date
    loan = next((l for l in loans if l.member_name == member_name
                 and l.book_id == book_id and not l.return_date), None)

    if not loan:
        return False, f"No active loan found for Member '{member_name}' with Book ID B{book_id}."

    # Mark the loan as returned
    loan.return_date = datetime.now().strftime('%Y-%m-%d')
    save_loans(loans)

    # Update book status to 'Available'
    update_book_status(book_id, "Available")

    return True, f"Book ID B{book_id} returned successfully on {loan.return_date}."


