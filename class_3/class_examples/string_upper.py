"""
str.lower()
str.upper()
str.capitalize()
str.startswith()
str.endswith()
str.split()
str.isinstace()
"""

# str.upper()
palabra = "Hola Mundo"

print(palabra.upper())  # HOLA MUNDO

respuesta = input("Ingrese la primera letra del abecedario: ")

if respuesta.upper() == "A":
    print("Eso es correcto!")
else:
    print("Eso es incorrecto!")
