"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
if score > 100:
    print("Invalid score")

elif score <= 49:
    print("Bad")
elif score <= 50:
    print("Passable")
elif score >= 90:
    print("Excellent")
else:
    print("Invalid score")


