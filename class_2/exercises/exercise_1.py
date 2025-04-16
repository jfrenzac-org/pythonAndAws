"""Description:
Create a program that accepts a list of numbers from the user (comma-separated) and calculates the
sum of only the odd numbers in that list.

Concepts Covered: Lists, for loops, input, print"""


def sum_odd(numbers):
    list_of_odds = [
        int(number.strip()) for number in numbers.split(",") if int(number.strip()) % 2 == 0
    ]

    return f"The list of odds is: {list_of_odds}, and their sum is: {sum(list_of_odds)}"


if __name__ == "__main__":
    numbers = input("Enter a list of numbers each separeted by comma: ")
    print(sum_odd(numbers))
