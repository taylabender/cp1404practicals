"""
CP1404/CP5632 Practical
Colour Names Dictionary
"""

NAME_TO_CODE = {"Amber": "#ffbf00", "Aqua": "#00ffff", "Ash Grey": "#b2beb5", "Baby Pink": "#f4c2c2",
                "Banana Yellow": "#ffe135", "Black": "#000000", "Blue Green": "#0d98ba",
                "Bronze": "#cd7f32", "Bubble Gum": "#ffc1cc", "Coffee": "#6f437",
                "Cream": "#fffdd0"}
print("colour names: \n Amber \n Aqua \n Ash Grey \n Baby Pink \n Banana Yellow \n "
      "Black \n Blue Green \n Bronze \n Bubble Gum \n Coffee \n Cream")

colour_name = input("Enter colour name for code information: ")

while colour_name != "":
    print(f" The code for \"{colour_name}\" is {NAME_TO_CODE.get(colour_name)}")
    colour_name = input("Enter colour name: ")

