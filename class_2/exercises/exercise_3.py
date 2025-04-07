"""Description:
Write a program that takes a number as input and prints the multiplication
 table for that number from 1 to 10.

Concepts Covered: for loops, input, print, range"""

#Pido al usuario ingresar el número
num = input("Ingrese el número: ")

try:
    num = int(num)
    for i in range(1,11):
        print(f"{num} * {i} = {i*num}")
except:
    print("Solo se pueden ingresar números")
