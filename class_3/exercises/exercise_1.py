"""Ejercicio 1: Conversión a mayúsculas

Enunciado:
Escribe una función que reciba una cadena de texto y devuelva la misma cadena
convertida a mayúsculas. No uses print(), la función debe retornar el resultado."""

from utils.exception_handler import exception_handler


@exception_handler
def convertir_en_mayusculas(texto: str) -> str:
    return texto.upper()


if __name__ == "__main__":
    texto = "abcdefghijk"
    print(convertir_en_mayusculas(texto))
