"""
Ejercicio 9: Letras de una palabra
Enunciado:
Crea una función que reciba una palabra como string y devuelva una lista
con cada una de sus letras como elementos separados.

"""


def letras_de_palabra(texto: str) -> list:
    return list(texto)


if __name__ == "__main__":
    texto = "This is the text that will serve as input"
    print(letras_de_palabra(texto))
