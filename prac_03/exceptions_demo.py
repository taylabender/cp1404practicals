"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    There is no ValueError.
    Decimal number cannot be used for the numerator or denominator

2. When will a ZeroDivisionError occur?
    When a zero is used for the denominator

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Get the user to input a valid number
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Cannot divide by zero!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Could not figure out how to fix it
