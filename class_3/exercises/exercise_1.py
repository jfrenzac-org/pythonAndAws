"""Ejercicio 1: Conversión a mayúsculas

Enunciado:
Escribe una función que reciba una cadena de texto y devuelva la misma cadena
convertida a mayúsculas. No uses print(), la función debe retornar el resultado."""

def mayus(text):
    mayus_text = text.upper()
    return mayus_text

user_text = input("Please enter the text you would like to convert to uppercase: ")
print(f"The text on uppercase is: {mayus(user_text)}")
