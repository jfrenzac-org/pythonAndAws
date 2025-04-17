"""
Ejercicio 2: Contar vocales
Enunciado:
Crea una función que reciba una cadena de texto y cuente cuántas
vocales contiene (a, e, i, o, u — tanto mayúsculas como minúsculas).
Devuelve ese número como resultado.

"""

def vocals (text):
    vocals = ["a","e","i","o","u"]
    text = text.lower()
    vocal_counter = 0
    for letter in text:
        if letter in vocals:
            vocal_counter += 1
    return vocal_counter

user_text = input("Ingrese una cadena de texto para contar las vocales en ella: ")   
print(f"Hay {vocals(user_text)} vocales en: {user_text}")
    

