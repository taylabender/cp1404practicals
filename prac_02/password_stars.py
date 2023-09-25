def main():
    while True:
        password = input("Enter a password: ")
        if len(password) < 8:
            print("Make sure password is at least 8 digits")
        elif not password.isdigit():
            print("Make sure password has a number")
        else:
            print("Password seems fine")
            break

main()
