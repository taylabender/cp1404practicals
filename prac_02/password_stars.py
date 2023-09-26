"""
Create program for a password with min length,
and display in asterisks.
Minimum length = 8
"""


# main() function
def get_password():
    def main():
        while True:
            password = input("Enter a password: ")
            if len(password) < 8:
                print("Make sure password is at least 8 digits")
            else:
                print('*' * len(password))
                break

    main()


get_password()


