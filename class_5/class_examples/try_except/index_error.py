"""
IndexError try - except block
"""

frutas = ["manzana", "pera"]

try:
    print(frutas[0])
    print(frutas[1])
    print(frutas[2])
except IndexError:
    print("El Indice no existe")
