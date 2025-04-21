"""
Ejercicio 3: Unir dos listas
Enunciado:
Define una función que reciba dos listas y las combine en una sola usando
el método extend(). La función debe retornar la lista resultante.

"""
hermanos = ["Beto", "Isidro", "Victor", "Rodrigo"]
hermanas = ["Cecilia", "Esther", "Berenice"]


def combinar_listas(hermanos, hermanas):
    lista_combinada = hermanos.copy()
    ## para no perder la original se copia la lista 1
    lista_combinada.extend(hermanas)
    return lista_combinada

resultado = combinar_listas(hermanos, hermanas)

print(resultado)
