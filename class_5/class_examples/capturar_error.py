"""
try - except - Capturar error.

Necesito conservar visibilidad sobre cuál except se está ejecutando

"""


def dividir_dos_numeros(numero1: int, numero2: int) -> int:
    return numero1 / numero2


try:
    print(dividir_dos_numeros(5, 0))
except ZeroDivisionError as e:
    print(f"Error: {e}")
except TypeError as e:
    print(f"Error: {e}")
finally:
    print("Terminé mi programa")
