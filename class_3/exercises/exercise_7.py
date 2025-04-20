"""
Ejercicio 7: Invertir una lista
Enunciado:
Crea una función que reciba una lista y devuelva una nueva lista con los mismos
elementos pero en orden inverso.
"""

lista = [1, 3, 8, 5, 7, 12, 9, 11, 5, 2, 4, 9, 6, 8, 13, 10]

def lista_inversa (lista):
    return lista [: : -1]

resultado = lista_inversa(lista) 

print(resultado)

