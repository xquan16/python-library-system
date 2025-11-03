
import librarian_info
import member_info

# Store user credentials (username: password)
users = {
    'HAO': '0706'
}

# Track the current logged-in user
current_user = None


def login():
    """Login function to authenticate users."""
    global current_user  # Use the global variable to track logged-in user

    print("\n=== Login ===")
    username = input("Enter Username: ").upper()
    password = input("Enter Password: ").upper()

    if username in users and users[username] == password:
        current_user = username  # Set the current user
        print(f"\n--- Welcome, {current_user}! You are now logged in. ---\n")
        return True
    else:
        print("\nInvalid username or password. Please try again.......\n")
        return False


def logout():
    """Logout function to reset the current user and exit."""
    global current_user  # Use global to modify the current user
    if current_user:
        print(f"\n--- {current_user} has logged out. ---")
        current_user = None  # Clear the current user
    print("Exiting the login system......")
    return  # Return control to the caller (if imported) instead of re-running the login loop


def main():
    """Login first, if login fails, stop the program."""
    if not login():
        return  # Stop execution if login fails

    """Main menu displayed after login."""
    while True:
        print("1. Member Information Management")
        print("2. Librarian Information Management")
        print("3. Log Out")

        choice = input("\nEnter your choice (1-3): ")

        if choice == '1':
            member_info.main()

        elif choice == '2':
            librarian_info.main()

        elif choice == '3':
            logout()
            print("\n--- Thank you for using the Library System. Goodbye! ---\n")
            break

        else:
            print("\nInvalid choice. Please try again......\n")


if __name__ == '__main__':
    main()