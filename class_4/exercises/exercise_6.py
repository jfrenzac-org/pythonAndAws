"""
Multiplicar cada número por 10 solo si es mayor que 5
Dada una lista de números, filtra aquellos mayores que 5 y multiplícalos por 10.
Entrada: [2, 6, 8, 3, 1]
Salida esperada: [60, 80]
Usa filter(), map() y lambda.
"""

numeros = [2, 6, 8, 3, 1]


multiplicados_por_diez = map(lambda x: x * 10, filter(lambda x: x > 5, numeros))

print(list(multiplicados_por_diez))
