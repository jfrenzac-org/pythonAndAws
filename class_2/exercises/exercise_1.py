## """Description:
## Create a program that accepts a list of numbers from the user (comma-separated) and calculates 
## the sum of only the odd numbers in that list.
## Concepts Covered: Lists, for loops, input, print"""

    ## Solicitar al usuario  que ingrese una lista de números separados por comas
entrada=input("Ingrese una lista de números separados por comas: ")
numeros=[int(num)for num in entrada.split(",")]
print(numeros)
## Filtra y suma solo los números impares
## Llamada a la función suma inpares.
suma_impares=sum(num for num in numeros if num%2!=0)
print("La suma de los numeros impares es: ", suma_impares)

suma_pares=sum(num for num in numeros if num%2==0)
print("La suma de los numeros impares es: ", suma_pares)

