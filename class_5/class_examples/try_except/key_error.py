"""
KeyError - try - except block

"""

frutas = {"fruta1": "mazana", "fruta2": "pera"}

try:
    print(frutas["fruta3"])
except KeyError:
    print("El diccionario no tiene esa llave")

try:
    print(frutas.get("fruta3", frutas.get("fruta1")))
except KeyError:
    print("La llave no existe")
