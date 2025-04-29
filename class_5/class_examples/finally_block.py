"""
try:
    # Operación riesgosa
except TipoDeExcepción:
    # Manejo de la excepción
finally:
    # Código que siempre se ejecuta

"""


def dividir_dos_numeros(numero1: int, numero2: int) -> int:
    return numero1 / numero2


try:
    print(dividir_dos_numeros(5, "e2"))
except ZeroDivisionError:
    print("No se puede dividir por cero")
except TypeError:
    print("La función solamente acepta números reales")
finally:
    print("Terminé mi programa")
