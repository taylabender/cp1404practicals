""" Write a standard structure that uses main and
other functions. The menu should have four separate
options. """

# display menu
menu_list = "(G)et valid score\n(P)rint result\n(S)show stars\n(Q)uit"
print(menu_list)


# While choice for menu
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "G":
        score = float(input("Enter score. Must be 0-100 inclusive:  "))
        break
    elif choice == "P":
        def score_status(score):
        print(score_status(score))
    elif choice == "S":
        print('*' * len(score))
        break
    else:
        print("Invalid key, try again")
        break
# print(menu_list)
choice = input(">>> ").upper()


