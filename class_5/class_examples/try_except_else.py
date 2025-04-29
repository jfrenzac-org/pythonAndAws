"""
try:
    # Operación riesgosa
except TipoDeExcepción:
    # Manejo de la excepción
else:
    # Código que se ejecuta si y solo si no hay excepciones

"""


def dividir_dos_numeros(numero1: int, numero2: int) -> int:
    return numero1 / numero2


try:
    print(dividir_dos_numeros(5, 2))
except ZeroDivisionError:
    print("no dividir por cero")
else:
    print("Estoy aqui!")
