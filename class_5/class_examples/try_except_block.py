"""
try:
    # Operación riesgosa
except TipoDeExcepción:
    # Manejo de la excepción
finally:
    # Código que siempre se ejecuta

"""

from decorador import exception_handler


@exception_handler
def dividir_dos_numeros(numero1: int, numero2: int) -> int:
    return numero1 / numero2


@exception_handler
def sumar_dos_numeros(numero1: int, numero2: int) -> int:
    pass


# try:
#     print(dividir_dos_numeros(5, 0))
# except ZeroDivisionError:
#     print("No es posible dividir por zero")

# print("Estoy aqui!")
