"""
str.lower()
str.upper()
str.capitalize()
str.startswith()
str.endswith()
str.split()
str.isinstace()
"""

palabra = "Hola Mundo"

# str.lower()
print(palabra.lower())  # hola mundo

respuesta = input("Ingrese la primera letra del abecedario: ")

if respuesta.lower() == "a":
    print("Eso es correcto!")
else:
    print("Eso no es correcto!")
