
def load_librarians():
    librarians = []
    try:
        with open(r'C:\Users\0216c\OneDrive\Desktop\APU\Python\Library System\library\staff.txt', 'r') as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 5:  # Ensure exactly 5 values
                    id, name, gender, city, phone_no = data
                    librarians.append((int(id), name, gender, city, phone_no))
                else:
                    print(f"Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
        print("Librarians file not found......")
    return librarians


def save_librarians(librarians):
    with open(r"C:\Users\0216c\OneDrive\Desktop\APU\Python\Library System\library\staff.txt", "w") as file:
        for mb in librarians:
            file.write(f'{mb[0]},{mb[1]},{mb[2]},{mb[3]},{mb[4]}\n')


def view_librarians(librarians):
    if not librarians:
        print("No librarian in the library system.")
    else:
        for mb in librarians:
            print(f'ID: S{mb[0]},\nName: {mb[1]},\nGender: {mb[2]},\n'
                  f'City: {mb[3]},\nPhone_No: {mb[4]}\n')


def add_librarian(librarians):
    print("\n Add New Librarian")
    print("Press 'q' or just press Enter at any time to return to the menu.")

    id_input = input('Librarian ID (or "q" to return): ')
    if not id_input.strip() or id_input.lower() == 'q': return
    id = int(id_input)

    name = input('Name (or "q" to return): ').upper()
    if not name.strip() or name == 'Q': return

    gender = input('Gender (M/F) (or "q" to return): ').upper()
    if not gender.strip() or gender == 'Q': return
    
    city = input('City (or "q" to return): ').upper()
    if not city.strip() or city == 'Q': return
    
    phone_no = input('Phone_No (or "q" to return): ')
    if not phone_no.strip() or phone_no.lower() == 'q': return

    librarians.append((id, name, gender, city, phone_no))  # Add as a tuple
    save_librarians(librarians)  # Save into txt file
    print("< Librarian added successfully. >")


def remove_librarian(librarians):
    id = int(input("Enter the Librarian ID to remove: S"))
    for mb in librarians:
        if mb[0] == id:  # Compare by ID (first element of tuple)
            librarians.remove(mb)
            save_librarians(librarians)  # Update txt file
            print("< Librarian removed successfully. >")
            return
    print("Librarian not found......")


def edit_librarian(librarians):
    id = int(input("Enter Librarian ID to edit: S"))
    for index, mb in enumerate(librarians):
        if mb[0] == id:
            name = input(f"Update Name (current: {mb[1]}): ").upper() or mb[1]
            gender = input(f"Update Gender(M/F) (current: {mb[2]}): ").upper() or mb[2]
            city = input(f'Update City (current: {mb[3]}): ').upper() or mb[3]
            phone_no = input(f'Update Phone.No (current: {mb[4]}): ') or mb[4]
            librarians[index] = (mb[0], name, gender, city, phone_no)  # Update the tuple
            save_librarians(librarians)
            print("< Librarian information updated successfully. >")
            return
    print("Librarian not found.")


def search_librarian(librarians):
    while True:
        print('\n1. Librarian ID')
        print('2. Name')
        print('3. Gender')
        print('4. City')
        print('5. Phone_No')
        print('6. Back')

        search = input('\nEnter your choice(1-6) to Search by: ')

        if search == '1':
            id = int(input("\nEnter Librarian ID: S"))

            found = False
            for mb in librarians:
                if mb[0] == id:
                    print(f'[ ID: S{mb[0]}, Name: {mb[1]}, Gender: {mb[2]}, City: {mb[3]}, Phone_No: {mb[4]} ]')
                    found = True
            if not found:
                print("\nLibrarian not found. Please try again......\n")

        elif search == '2':
            name = input("\nEnter Librarian Name: ").upper()

            found = False
            for mb in librarians:
                if mb[1] == name:
                    print(f'[ ID: S{mb[0]}, Name: {mb[1]}, Gender: {mb[2]}, City: {mb[3]}, Phone_No: {mb[4]} ]')
                    found = True
            if not found:
                print("\nLibrarian not found. Please try again......\n")

        elif search == '3':
            gender = input("\nEnter Gender(M/F): ").upper()

            found = False
            for mb in librarians:
                if mb[2] == gender:
                    print(f'[ ID: S{mb[0]}, Name: {mb[1]}, Gender: {mb[2]}, City: {mb[3]}, Phone_No: {mb[4]} ]')
                    found = True
            if not found:
                print("\nLibrarian not found. Please try again......\n")

        elif search == '4':
            city = input("\nEnter City: ").upper()

            found = False
            for mb in librarians:
                if mb[3] == city:
                    print(f'[ ID: S{mb[0]}, Name: {mb[1]}, Gender: {mb[2]}, City: {mb[3]}, Phone_No: {mb[4]} ]')
                    found = True
            if not found:
                print("\nLibrarian not found. Please try again......\n")

        elif search == '5':
            phone = input("\nEnter Phone_No: ")

            found = False
            for mb in librarians:
                if mb[4] == phone:
                    print(f'[ ID: S{mb[0]}, Name: {mb[1]}, Gender: {mb[2]}, City: {mb[3]}, Phone_No: {mb[4]} ]')
                    found = True
            if not found:
                print("\nLibrarian not found. Please try again......\n")

        elif search == '6':
            break

        else:
            print("\nInvalid choice. Please try again......")


def main():
    librarians = load_librarians()

    while True:
        print("\n--- Librarians Information Management ---")
        print(f"[Loaded {len(librarians)} librarians.]\n")  # Verify how many librarians were loaded
        print("1. View All Librarians")
        print("2. Add New Librarian")
        print("3. Remove Librarian")
        print("4. Edit Librarian Information")
        print("5. Search Librarian Information")
        print("6. Back")

        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            print('\n<All Librarians>')
            view_librarians(librarians)

        elif choice == '2':
            print('\n<All Librarians>')
            view_librarians(librarians)
            print('\n<Add New Librarian>')
            add_librarian(librarians)

        elif choice == '3':
            print('\n<All Librarians>')
            view_librarians(librarians)
            print('\n<Remove Librarian>')
            remove_librarian(librarians)

        elif choice == '4':
            print('\n<All Librarians>')
            view_librarians(librarians)
            print('\n<Edit Librarian Information>')
            edit_librarian(librarians)

        elif choice == '5':
            print('\n<Search Librarian Information>')
            search_librarian(librarians)

        elif choice == '6':
            print("\n--- Thank you for using the Library Librarians System. Goodbye! ---\n")
            break
        else:
            print("\nInvalid choice. Please try again......\n")


if __name__ == '__main__':
    main()

