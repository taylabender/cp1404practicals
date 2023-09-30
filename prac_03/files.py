"""
1) Write code that asks the user for their name,
then opens a file called "name.txt" and writes
that name to it. Remember to close your file.

2) Write code that opens "name.txt" and reads the
name (as above) then prints, "Your name is Bob"
(or whatever the name is in the file)

3) Create a text file called numbers.txt and save
it in your prac directory. Put the following three
numbers on separate lines in the file and save it:
17
42
400
Write code that opens "numbers.txt", reads only the
first two numbers and adds them together then prints
the result, which should be... 59.

4) Now write a fourth block of code that prints the
total for all lines in numbers.txt or a file with
any number of numbers.
"""

# Task 1
FILENAME = "name.txt"
name = input("Enter your name: ")
out_file = open(FILENAME, "w")


# Task 2
print(f"Your name is: {name}", file=out_file)
out_file.close()


# Task 3
in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print(number1 + number2)

in_file.close()


