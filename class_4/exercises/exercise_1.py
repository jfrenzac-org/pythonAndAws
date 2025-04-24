"""
Elevar al cuadrado cada número
Dado un listado de números, obtén una nueva lista con cada número elevado al cuadrado.
Entrada: [1, 2, 3, 4, 5]
Salida esperada: [1, 4, 9, 16, 25]

Usa map() con una función lambda.
"""

## numeros = [1, 2, 3, 4, 5]

##def eleve_al_cuadrado (numero: int) -> int:
   ## return numero ** 2


numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x:  x**2, numeros))

print(cuadrados)