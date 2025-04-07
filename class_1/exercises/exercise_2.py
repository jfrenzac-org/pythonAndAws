# Write a program that asks the user for a number and determines whether
#  it is even or odd.

num = input("Ingrese un número entero: ")
try:
    num = int(num)
    remainder = num%2
    
    if remainder == 0:
        print(f"El número {num} es par")
    else:
        print(f"El número {num} es impar")
except:
    print("Solo se pueden ingresar números enteros")