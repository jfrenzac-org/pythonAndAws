"""
Ejercicio 6: Contar elementos en lista
Enunciado:
Define una función que reciba una lista y un valor, y devuelva cuántas
veces aparece ese valor en la lista utilizando el método count().

"""
lista = [1, 3, 8, 5, 7, 12, 9, 11, 5, 2, 4, 9, 6, 8, 13, 10]
valor =int(input("Escoja un número de la lista: "))

def contar_apariciones (lista, dato):
    return lista.count(dato)

resultado = contar_apariciones(lista, valor)

print(f"El valor elegido es {valor} y aparece {resultado} veces en la lista.")


