
import SA  # 1.
import LB  # 2.
import l_member  # 3.


def main():
    while True:
        print("\n~~~ Welcome To Library ~~~")
        print('1. System Administrator')
        print('2. Librarian')
        print('3. Library Member')
        print('4. Exit')

        try:
            user = int(input('\nEnter your choice(1-4) \nWho are you?: '))

            if user == 1:
                print('\n~~~ Welcome, System Administrator! ~~~')
                SA.main()

            elif user == 2:
                print('\n~~~ Welcome, Librarian! ~~~')
                LB.main()  # Call the function from book.py

            elif user == 3:
                print('\n~~~ Welcome, Library Member~~~')
                l_member.main()

            elif user == 4:
                print('\nExiting the system......\n')
                break

            else:
                print('\nError, invalid option. Please try again.')

        except ValueError:
            print('\nInvalid input. Please enter a number between 1 and 4.')


if __name__ == '__main__':
    main()
















