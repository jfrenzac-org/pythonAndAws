# Write a program that asks the user for a number and determines whether
#  it is even or odd.

#Cre un ciclo try para analizar si el usuario ingresa un número
num = input("Ingrese un número entero: ")
try:
    #Almaceno el valor ingresado por el usuario y lo convierto en int
    num = int(num)
    """
    Hallo el residuo de la división del número dividido por dos para
    verificar si es par o impar
    """
    remainder = num%2
    
    #Creo un ciclo que nos dice si el número es par o impar
    if remainder == 0:
        print(f"El número {num} es par")
    else:
        print(f"El número {num} es impar")
#Con este except manejo los valores no numéricos ingresados por el usuario
except:
    print("Solo se pueden ingresar números enteros")