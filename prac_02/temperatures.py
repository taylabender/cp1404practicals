"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

# Write this section to convert F to C and display the result
# Hint: celsius = 5 / 9 * (fahrenheit - 32)
# Remove the "pass" statement when you are done. It's a placeholder.


MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def convert_c_to_f():
    global celsius, fahrenheit
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32


def convert_f_to_c():
    global fahrenheit, celsius
    fahrenheit = float(input("fahrenheit"))
    celsius = 5 / 9 * (fahrenheit - 32)


while choice != "Q":
    if choice == "C":
        convert_c_to_f()
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        convert_f_to_c()
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
