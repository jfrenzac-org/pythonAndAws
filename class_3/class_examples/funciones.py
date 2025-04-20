# def ---> definition
# return --- Retornar
# isinstance --> Validar el tipo de dato de una variable


def sumar_numeros(numero_1, numero_2):
    if isinstance(numero_1, int) and isinstance(numero_2, int):
        return numero_1 + numero_2
    else:
        return f"Los argumentso deben ser números enteros y {numero_1} es {type(numero_1)}"


print(sumar_numeros("3", 2))
