"""
Ejercicio 8: Eliminar espacios sobrantes

Enunciado:

Escribe una función que reciba un string y devuelva ese mismo string sin los
espacios en blanco al principio ni al final. Usa el método strip().
"""

## creemos  un string con varios espacios en blanco al comienzo y al final

texto = "   Esta cadena de texto tiene varios espacios en blanco al comienzo y al final.   "

def quitar_espacios(string):
    return string.strip()

resultado = quitar_espacios(texto)

print(f'Este es el "{resultado}".')

