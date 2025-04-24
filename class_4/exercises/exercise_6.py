"""
Multiplicar cada número por 10 solo si es mayor que 5
Dada una lista de números, filtra aquellos mayores que 5 y multiplícalos por 10.
Entrada: [2, 6, 8, 3, 1]
Salida esperada: [60, 80]
Usa filter(), map() y lambda.
"""

numeros = [2, 3, 5, 8, 4, 5, 7, 10, 6]

mayores_que_5 = list(filter(lambda x: True if x > 5 else False, numeros))

## print(mayores_que_5)  8, 7, 10, 6

por_diez = list(map(lambda x: x * 10, mayores_que_5))


print(por_diez)

