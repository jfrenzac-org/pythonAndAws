"""
Ejercicio 5: Buscar palabra en texto
Enunciado:
Crea una función que reciba un texto largo y una palabra, y determine
si esa palabra está contenida dentro del texto. La función debe devolver True o False.

"""
texto = ("la palabra testigo debe estar contenida en el texto inicial, luego cada palabra que sea elegida "
"por el usuario será evaluada y se definirá como falsa o verdadera en su pertenencia al texto.")

palabra_elegida = input("Ingrese una palabra: ") 

##lista_palabras = list(texto.split())
## print(lista_palabras)

def contiene_palabra_elegida (texto, palabra_elegida):
    return palabra_elegida in texto

resultado = contiene_palabra_elegida (texto.lower(), palabra_elegida.lower())
if resultado == True:

    print(resultado)

    print(f"La palabra elegida es '{palabra_elegida}' y está contenida en el texto.")

else:
    print(resultado)
    print(f"La palabra elegida es: '{palabra_elegida}'  y no está en el texto.")






