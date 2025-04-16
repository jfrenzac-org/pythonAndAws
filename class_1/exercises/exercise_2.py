# Write a program that asks the user for a number and determines whether
#  it is even or odd.


def is_even(number: int) -> str:
    if number % 2 == 0:
        return f"'{number}' is even"
    else:
        return f"'{number}' is odd"


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(is_even(number))
