"""Description:
Create a program that accepts a list of numbers from the user (comma-separated) and calculates the
sum of only the odd numbers in that list.

Concepts Covered: Lists, for loops, input, print"""

# Accept input from the user
user_input = input("Enter a list of numbers (comma-separated): ")

# Convert the input string into a list of integers
number_list = [int(num.strip()) for num in user_input.split(',')]

# Initialize the total to 0
total = 0

# Iterate through the list of numbers
for num in number_list:
    if num % 2 != 0:  # Check if the number is odd
        total += num   # Add the odd number to the total

# Print the result
print(f"The sum of odd numbers in the list is: {total}")