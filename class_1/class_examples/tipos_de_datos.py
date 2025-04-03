# Casting -- Transformat un tipo de dato a otro
# str == string == cadena de letras
# int == integer == número entero
# float == flotante -- decimal
# Opero: float + int == float
# list == Lista
# type() -> Validar la clase a la que pertenece mi objeto

numero = float(input("Ingrese un número: "))
print(f"Respuesta: El dato '{numero}' tiene tipo: {type(numero)}")
print(numero + 2)
