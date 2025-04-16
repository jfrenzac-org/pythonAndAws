"""
Ejercicio 5: Buscar palabra en texto
Enunciado:
Crea una función que reciba un texto largo y una palabra, y determine
si esa palabra está contenida dentro del texto. La función debe devolver True o False.

"""


def palabra_en_texto(texto: str, palabra: str) -> bool:
    return palabra in texto


if __name__ == "__main__":
    texto = "This is the text where the function will look for the word"
    palabra = "This"

    print(palabra_en_texto(texto.lower(), palabra.lower()))
