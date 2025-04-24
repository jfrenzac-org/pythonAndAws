"""
Filtrar números pares

Filtra de una lista los números que sean pares.

Entrada: [1, 2, 3, 4, 5, 6]
Salida esperada: [2, 4, 6]
Usa filter() con lambda.
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

## solamente con la función filter con lambda se obtiene el resultado.
pares = list(filter(lambda x: True if x % 2 == 0 else False, numeros))

print(pares)