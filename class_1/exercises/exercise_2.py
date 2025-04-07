# Write a program that asks the user for a number and determines whether
#  it is even or odd.

# Taking user input
number = int(input("Please write a number and we will determine if it is even or odd: "))

# Condition
# % is modulo operator. If that's zero then the number is even
if   number%2 == 0:
     print(number, "is even")
     print("________") 
else:
     print(number, "is odd")
     print("________")