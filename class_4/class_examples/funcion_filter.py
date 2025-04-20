# map()
# lambda

# filter()

# list()

"""
Funciones de Order Superior: Es una función que cumple al menos 1 de los
siguientes:

1. Recibe una o más funciones como argumento
2. Devuleve una función como resultado
"""

# map()


def es_par(numero: int) -> bool:
    if numero % 2 == 0:
        return True
    return False


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter()

resultados = list(filter(es_par, numeros))

resultados = list(filter(lambda x: True if x % 2 == 0 else False, numeros))

print(resultados)
