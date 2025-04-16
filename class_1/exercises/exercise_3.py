"""Write a program that asks the user for a score (0 to 100) and prints the
 corresponding letter grade based on the following scale:

90 or more: "A"

80 to 89: "B"

70 to 79: "C"

60 to 69: "D"

Below 60: "F""
"""


def grade_on_score(score: str) -> str:

    if score < 60:
        return "F"
    elif score <= 69:
        return "D"
    elif score <= 79:
        return "C"
    elif score <= 89:
        return "B"
    else:
        return "A"


if __name__ == "__main__":
    score = input("Enter a grade betweet 0 and 100: ")
    if not isinstance(score, int) or score > 100 or score < 0:
        print("The score must be an integer between 0 and 100")
    else:
        print(grade_on_score(int(score)))
