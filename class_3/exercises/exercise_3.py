"""
Ejercicio 3: Unir dos listas
Enunciado:
Define una función que reciba dos listas y las combine en una sola usando
el método extend(). La función debe retornar la lista resultante.

"""


def unir_dos_listas(lista1: list, lista2: list) -> list:
    lista1.extend(lista2)
    return lista1


if __name__ == "__main__":
    lista1 = [1, 2, 3, 4, 5]
    lista2 = [6, 7, 8, 9, 10]
    print(unir_dos_listas(lista1, lista2))
