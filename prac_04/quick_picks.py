"""
Quick pick program

"""

import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45

def main():
    """ prompt user how many quick picks they want"""
    quick_pick_number = int(input("How many quick picks? "))
    while quick_pick_number <= 0:
        print("invalid number")
        quick_pick_number = int(input("How many quick picks? "))

    for i in range(quick_pick_number):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))


main()