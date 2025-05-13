# Crear un programa que itere sobre una lista de numeros y
# genere otra lista de solamente los números pares que están en la
# lista 1

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lista de forma 'larga'
numeros_pares = []
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)

# Lista utilizando list comprehension
# [expresion for item in iterable if condition]

numeros_pares_con_comprension = [numero for numero in numeros if numero % 2 == 0]

print(numeros_pares)
print(numeros_pares_con_comprension)
