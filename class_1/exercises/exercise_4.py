"""
Write a program that asks the user for their age and classifies
 them into groups:

0-12 years: Child

13-19 years: Teenager

20-64 years: Adult

65 or more: Senior
"""


def classify_age(number: int) -> str:
    if age >= 65:
        return "Senior"
    elif age >= 20:
        return "Adult"
    elif age >= 13:
        return "Teenager"
    else:
        return "Child"


if __name__ == "__main__":
    age = int(input("Enter your age: "))
    if age < 0:
        print("Age must be a positive integer")
    else:
        print(classify_age(age))
