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

# Aplicar la función 'es_par' a todos los elementos de 'numeros' usando un
# ciclo 'for'

resultados = []
for numero in numeros:
    resultados.append(es_par(numero))

# Misma lógica, usando únicamente la función 'map()'
resultados = map(es_par, numeros)

# Usando función lambda
resultados = list(map(lambda x: True if x % 2 == 0 else False, numeros))

# Sintaxis Lambda

# lambda <variable_iteracion> : resultado_verdadero if <expresión bool> else resultado falso

print(resultados)
