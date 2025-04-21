"""
Ejercicio 9: Letras de una palabra
Enunciado:
Crea una función que reciba una palabra como string y devuelva una lista
con cada una de sus letras como elementos separados.

"""
palabra = input("ingresa una palabra: ")

def letras_palabra(palabra):
    return list(palabra)

resultado = list(palabra)

## Se imprime esto: ['P', 'y', 't', 'h', 'o', 'n'] como resultado