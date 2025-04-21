"""Ejercicio 1: Conversión a mayúsculas

Enunciado:
Escribe una función que reciba una cadena de texto y devuelva la misma cadena
convertida a mayúsculas. No uses print(), la función debe retornar el resultado."""

## pedimos una frase al usuario.

frase = input("ingresa una frase: ")
def convierte_a_mayuscula(frase):
    return frase.upper()

resultado = frase.upper()

print(resultado)
