# Lista de nombres

nombres = ["Ana", "Luis", "Ana", "Carlos", "Luis"]

# Eliminar duplicados con un ciclo y un condicional
nombres_unicos = []

for nombre in nombres:
    if nombre not in nombres_unicos:
        nombres_unicos.append(nombre)

# Eliminar duplicados usando set
nombres_unicos_con_set = set(nombres)

print(nombres_unicos)
print(nombres_unicos_con_set)
