"""
Ejercicio 7: Invertir una lista
Enunciado:
Crea una función que reciba una lista y devuelva una nueva lista con los mismos
elementos pero en orden inverso.
"""


def invertir_lista(lista: list[any]) -> list:
    lista.sort(reverse=True)
    return lista


if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(invertir_lista(lista))
