"""Description:
Write a program that takes a number as input and prints the multiplication
 table for that number from 1 to 10.

Concepts Covered: for loops, input, print, range"""

# Accept input from the user
user_input = int(input("Enter a number: "))

# Create iteration
for i in range(1, 11):
    print(i*user_input)
