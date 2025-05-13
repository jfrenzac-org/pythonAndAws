"""
Crear una tupla, acceder a sus elementos
- Contar cuantas veces aparece un valor
"""

# Crear una tupla

colores = ("rojo", "azul", "verde", "azul", "amarillo")

print(colores)

# Acceder al segundo valor
print("Segundo color:", colores[1])

# Contar cuántas veces aparece 'azul'

print("Veces que aparece 'azul': ", colores.count("azul"))
print(f"Veces que aparece 'azul': {colores.count("azul")}")

# Obtener el indice de 'verde'
print("Índice de 'verde': ", colores.index("verde"))
