frutas = {"manzana", "pera"}

# Agregar una fruta
frutas.add("naranja")
print("Despues de agregar: ", frutas)

# Intentar agregar un duplicado
frutas.add("naranja")
print("Después de agregar duplicado: ", frutas)

# Eliminar una fruta
frutas.remove("pera")
print("Después de eliminar: ", frutas)

# Eliminar con seguridad (sin error si el elemento no existe)
frutas.discard("uva")
print("Después de intentar eliminar 'uva': ", frutas)
