"""
Convertir una lista de enteros en booleanos (par=True, impar=False)

Convierte una lista de números enteros en una lista de booleanos indicando si el número es par.
Entrada: [1, 2, 3, 4]
Salida esperada: [False, True, False, True]
Usa map() con lambda.
"""

numeros = [1, 2, 3, 4]

es_par_bool = map(lambda x: True if x % 2 == 0 else False, numeros)

print(list(es_par_bool))
