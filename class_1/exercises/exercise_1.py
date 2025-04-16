# Write a program that asks the user for a number and classifies it as
# positive, negative, or zero.


def classify_number(number: int) -> str:
    if number == 0:
        return "The number is Zero"
    elif number > 0:
        return f"The number '{number}' is a positive integer"
    else:
        return f"The number '{number}' is a negative integer"


if __name__ == "__main__":

    number = int(input("Enter a Number: "))
    print(classify_number(number))
