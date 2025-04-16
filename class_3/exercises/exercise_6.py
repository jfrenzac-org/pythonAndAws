"""
Ejercicio 6: Contar elementos en lista
Enunciado:
Define una función que reciba una lista y un valor, y devuelva cuántas
veces aparece ese valor en la lista utilizando el método count().

"""


def contar_elementos(lista: list, valor: any) -> int:
    return lista.count(valor)


if __name__ == "__main__":
    lista = [1, 2, 3, 4, 1, 1, 1]
    valor = 1
    print(contar_elementos(lista, valor))
