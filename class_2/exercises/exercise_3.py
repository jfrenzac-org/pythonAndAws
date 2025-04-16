"""Description:
Write a program that takes a number as input and prints the multiplication
 table for that number from 1 to 10.

Concepts Covered: for loops, input, print, range"""


def multiplication_table(number: int) -> str:
    mult_table = f"The Multiplication table for {number} is\n"

    for i in range(1, 11):
        mult_table += f"{number} X {i} = {number*i}\n"

    return mult_table


if __name__ == "__main__":
    number = int(input("Enter an integer: "))
    print(multiplication_table(number))
