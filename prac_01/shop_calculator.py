"""
A shop requires a small program that would allow them to
quickly work out the total price for a number of items,
each with different prices.

The program allows the user to enter the number of items
and the price of each different item. Then the program
computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is
applied to that total before the amount is displayed on
the screen.
"""


# Prompt the user for the number of items
num_of_items = int(input("Number of items: "))

# Invalid number of items
while num_of_items < 0:
    print("Invalid number of items")
    num_of_items = int(input("Number of items:"))

# Price of items
total = 0
for i in range(num_of_items):
    price = float(input("Price of item:"))
    total += price

# 10% discount when the total price is over $100
if total > 100:
   total *= 0.9

print("total price for", num_of_items, "items is $", format(total, ".2f"))


