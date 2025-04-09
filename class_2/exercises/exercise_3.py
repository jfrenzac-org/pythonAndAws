"""Description:
Write a program that takes a number as input and prints the multiplication
 table for that number from 1 to 10.

Concepts Covered: for loops, input, print, range"""
## Generamos un número pedido al usuario que será el multiplicador y un rango de multiplicandos en una lista.

## multiplicador = numero
##multiplicandos = lista

lista = list(range(1, 11))
print(lista)

numero = int(input("Ingrese un número: "))

print(f"Tabla de multiplicar del No. {numero}: ")

for i in lista:
    producto = numero * i
    print(f"({numero} * {i} = {producto}")

