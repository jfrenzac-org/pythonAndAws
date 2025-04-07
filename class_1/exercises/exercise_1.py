# Write a program that asks the user for a number and classifies it as
# positive, negative, or zero.

number = float(input("Please write a number: "))

if   number > 0:
     print("The number is positive")
     print("________") 
elif number < 0:
     print("The number is negative")
     print("________")
else:
     print("The number is zero")
     print("________")