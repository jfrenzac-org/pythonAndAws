# Write a program that asks the user for a number and classifies it as
# positive, negative, or zero.

try:
    string_num = input("Ingrese un número entero ")
    num = int(string_num)
    if num < 0:
        print(f"El número {num} es negativo")
    elif num == 0:
        print(f"El número ingresado es igual a cero")
    else:
        print(f"El número {num} es positivo")
except:
    print("Solo se pueden ingresar números")  
    
