"""
ValueError -- try - except block
"""


def solicitar_numero():
    try:
        numero = int(input("Ingrese un número entero: "))
        return f"El número ingresado es: {numero}"
    except ValueError:
        print("Error: El valor ingresado no es un número entero válido")


print(solicitar_numero())
