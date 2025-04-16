"""
Ejercicio 2: Contar vocales
Enunciado:
Crea una función que reciba una cadena de texto y cuente cuántas
vocales contiene (a, e, i, o, u — tanto mayúsculas como minúsculas).
Devuelve ese número como resultado.

"""


def contar_vocales(texto: str) -> int:
    vocales = {"a", "e", "i", "o", "u"}  # Esta estructura de datos no la hemos visto, se llama set
    return sum(1 for letra in texto.lower() if letra in vocales)


if __name__ == "__main__":
    texto = "This is the text that will work as input for my function"
    print(contar_vocales(texto))
