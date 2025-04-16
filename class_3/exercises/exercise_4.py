"""Ejercicio 4: Palabras como lista
Enunciado:
Crea una función que reciba una frase (string) y devuelva una lista donde
cada palabra de la frase sea un elemento, usando espacios como separadores."""


def lista_desde_texto(texto: str) -> list:
    return texto.strip().split()


if __name__ == "__main__":
    texto = "This is the text that will be transformed into a list"
    print(lista_desde_texto(texto))
