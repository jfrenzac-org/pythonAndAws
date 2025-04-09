"""Description:
You are given two lists: one with keys and the other with values.
Create a dictionary by pairing the elements of the two lists.

Concepts Covered: Lists, dictionaries, for loops, zip(), items()"""

## Generamos las dos listas: alimentos, precios.

alimento = ["café", "chocolate", "azúcar", "panela", "arroz", "carne"]
precio = [15000, 12000, 4000, 4500, 21000, 38000]

## Creamos un diccionario vacio, con la etiqueta costos y allí hacemos el emparejamiento.

costos = {}

for alimento, precio in zip (alimento, precio):
    costos [alimento] = precio

print (costos)


