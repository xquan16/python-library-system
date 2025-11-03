
# 1. View All Member
# 2. Add New Member
# 3. Remove Member
# 4. Edit Member Information
# 5. Search Member Information
# 6. Back

def load_members():
    members = []
    try:
        with open(r"C:\chris\APU\Y1 Sem1\Python\Library System Code\members.txt", 'r') as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 5:  # Ensure exactly 5 values
                    id, name, gender, city, phone_no = data
                    member = {
                        "id": int(id),
                        "name": name,
                        "gender": gender,
                        "city": city,
                        "phone_no": phone_no
                    }
                    members.append(member)
                else:
                    print(f"Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
        print("Members file not found......")
    return members


def save_members(members):
    with open(r"C:\Users\0216c\OneDrive\Desktop\APU\Python\Library System\library\members.txt", "w") as file:
        for mb in members:
            file.write(f'{mb["id"]},{mb["name"]},{mb["gender"]},{mb["city"]},{mb["phone_no"]}\n')


def view_members(members):
    if not members:
        print("No member in the library system.")
    else:
        for mb in members:
            print(f'ID: M{mb["id"]},\nName: {mb["name"]},\nGender: {mb["gender"]},\n'
                  f'City: {mb["city"]},\nPhone_No: {mb["phone_no"]}\n')


def add_member(members):
    print("\n--- Add New Member ---")
    print("Press 'q' or just press Enter at any time to return to the menu.")

    id_input = input('Member ID (or "q" to return): ')
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

    member = {
        "id": id,
        "name": name,
        "gender": gender,
        "city": city,
        "phone_no": phone_no
    }
    members.append(member)
    save_members(members)
    print("\n< Member added successfully. >")


def remove_member(members):
    id = int(input("Enter the Member ID to remove: M"))
    for mb in members:
        if mb["id"] == id:
            members.remove(mb)
            save_members(members)
            print("< Member removed successfully. >")
            return
    print("\nMember not found......")


def edit_member(members):
    id = int(input("Enter Member ID to edit: M"))
    for mb in members:
        if mb["id"] == id:
            mb["name"] = input(f"Update Name (current: {mb['name']}): ").upper() or mb["name"]
            mb["gender"] = input(f"Update Gender(M/F) (current: {mb['gender']}): ").upper() or mb["gender"]
            mb["city"] = input(f'Update City (current: {mb["city"]}): ').upper() or mb["city"]
            mb["phone_no"] = input(f'Update Phone.No (current: {mb["phone_no"]}): ') or mb["phone_no"]
            save_members(members)
            print("< Member information updated successfully. >")
            return
    print("\nMember not found......")


def search_member(members):
    while True:
        print('\n1. Member ID')
        print('2. Name')
        print('3. Gender')
        print('4. City')
        print('5. Phone_No')
        print('6. Back')

        search = input('\nEnter your choice(1-6) to Search by: ')

        if search == '1':
            id = int(input("\nEnter Member ID: M"))

            found = False
            for mb in members:
                if mb["id"] == id:
                    print(f'[ {mb} ]')
                    found = True
            if not found:
                print("\nMember not found. Please try again......\n")

        elif search == '2':
            name = input("\nEnter Member Name: ").upper()

            found = False
            for mb in members:
                if mb["name"] == name:
                    print(f'[ {mb} ]')
                    found = True
            if not found:
                print("\nMember not found. Please try again......\n")

        elif search == '3':
            gender = input("\nEnter Gender(M/F): ").upper()

            found = False
            for mb in members:
                if mb["gender"] == gender:
                    print(f'[ {mb} ]')
                    found = True
            if not found:
                print("\nMember not found. Please try again......\n")

        elif search == '4':
            city = input("\nEnter City: ").upper()

            found = False
            for mb in members:
                if mb["city"] == city:
                    print(f'[ {mb} ]')
                    found = True
            if not found:
                print("\nMember not found. Please try again......\n")

        elif search == '5':
            phone = input("\nEnter Phone_No: ")

            found = False
            for mb in members:
                if mb["phone_no"] == phone:
                    print(f'[ {mb} ]')
                    found = True
            if not found:
                print("\nMember not found. Please try again......\n")

        elif search == '6':
            break

        else:
            print("\nInvalid choice. Please try again......\n")


def main():
    members = load_members()
    while True:
        print("\n--- Members Information Management ---")
        print(f"[Loaded {len(members)} members.]\n")
        print("1. View All Members")
        print("2. Add New Member")
        print("3. Remove Member")
        print("4. Edit Member Information")
        print("5. Search Member Information")
        print("6. Back")

        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            print('\n<All Members>')
            view_members(members)

        elif choice == '2':
            print('\n<Add New Member>')
            add_member(members)

        elif choice == '3':
            print('\n<Remove Member>')
            remove_member(members)

        elif choice == '4':
            print('\n<Edit Member Information>')
            edit_member(members)

        elif choice == '5':
            print('\n<Search Member Information>')
            search_member(members)

        elif choice == '6':
            print("\n--- Thank you for using the Library Members System. Goodbye! ---\n")
            break
        else:
            print("\nInvalid choice. Please try again......\n")



if __name__ == '__main__':
    main()