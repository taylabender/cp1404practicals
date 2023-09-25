"""
Program to determine score status using functions
"""

def main():
    # get user to input score
    global score
    score = float(input("Enter score: "))
    print(score_status(score))


def score_status(score):
    # determine status of score
    if score < 0:
        print("Invalid score")
    if score > 100:
        print("Invalid score")

    elif score >= 90:
        print("Excellent")
    elif score <= 50:
        print("Passable")
    else:
        print("Bad")

main()



