# display menu
menu_list = "(H)ello\n(G)oodbye\n(Q)uit"
name = input("Enter your name: ")
print(menu_list)

# while loop for menu choice
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("hello", name)
        break
    elif choice == "G":
        print("goodbye", name)
        break
    else:
        print("Invalid key, try again")
        break
print(menu_list)
choice = input(">>> ").upper()



