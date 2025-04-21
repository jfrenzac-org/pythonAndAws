"""
Filtrar números pares

Filtra de una lista los números que sean pares.

Entrada: [1, 2, 3, 4, 5, 6]
Salida esperada: [2, 4, 6]
Usa filter() con lambda.
"""

numeros = [1, 2, 3, 4, 5, 6]
numeros_pares = filter(lambda x: x % 2 == 0, numeros)

print(list(numeros_pares))
