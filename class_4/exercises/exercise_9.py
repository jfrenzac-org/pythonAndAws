"""
Sumar los elementos de dos listas (elemento a elemento)
Dados dos listas del mismo tamaño, obtener una lista con la suma elemento a elemento.
Entrada: [1, 2, 3], [4, 5, 6]
Salida esperada: [5, 7, 9]
Usa map() con lambda y múltiples argumentos.
"""

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

sumatoria = map(lambda x, y: x + y, lista1, lista2)

print(list(sumatoria))
