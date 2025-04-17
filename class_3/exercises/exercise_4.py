"""Ejercicio 4: Palabras como lista
Enunciado:
Crea una función que reciba una frase (string) y devuelva una lista donde
cada palabra de la frase sea un elemento, usando espacios como separadores."""

def separate_words(text):
    words = []
    text.strip()
    words.append(text.split())
    return words

print(separate_words("separador de frases en palabras"))