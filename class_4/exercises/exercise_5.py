"""
Convertir una lista de enteros en booleanos (par=True, impar=False)

Convierte una lista de números enteros en una lista de booleanos indicando si el número es par.
Entrada: [1, 2, 3, 4]
Salida esperada: [False, True, False, True]
Usa map() con lambda.
"""
## Con una línea de código usando la función map y una lambda.

numeros = [2, 4, 7, 12, 9, 11, 14, 19, 16]

resultados = list(map(lambda x : True if x % 2 == 0 else False, numeros))

print(resultados)