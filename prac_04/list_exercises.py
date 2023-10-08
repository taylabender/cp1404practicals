""" Intermediate exercises
Basic list operations - Prompt user for 5 numbers,
    then stores each of these in a list.

Woefully inadequate security checker - ask user for
    their username.

"""

# 1) Basic list operations
numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

print("The first number is ", )
print("The last number is ")
print("The smallest number is", min(numbers))
print("The largest number is ", max(numbers))
print("The average of the numbers is ", sum(numbers)/5)


# 2) Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
             'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole',
             'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter username")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")


