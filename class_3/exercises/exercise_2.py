"""
Ejercicio 2: Contar vocales
Enunciado:
Crea una función que reciba una cadena de texto y cuente cuántas
vocales contiene (a, e, i, o, u — tanto mayúsculas como minúsculas).
Devuelve ese número como resultado.

"""

## Se genera una cadena y se convierte a letras minúsculas.
## En la lista de vocales se incluyen aquellas que puedan tener diéresis o tilde.

cadena = ("Cuántas vocales hay en éstas PALABRAS, averigüelo.")
vocales = ("aeiouáéíóúü")
contador = 0

for letra in cadena.lower():
    if letra in vocales:
        contador += 1

print("La cantidad de Vocales en la cadena es: ", contador)

