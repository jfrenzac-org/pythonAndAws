"""
Extraer los números negativos
Filtra una lista de enteros para obtener sólo los negativos.
Entrada: [5, -1, -7, 2, -3]
Salida esperada: [-1, -7, -3]
Usa filter() con lambda.
"""

numeros = [5, -1, -7, 2, -3]

negativos = filter(lambda x: x < 0, numeros)

print(list(negativos))
