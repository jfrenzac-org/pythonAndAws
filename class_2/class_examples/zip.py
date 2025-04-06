# zip()

frutas = ["manzana", "pera", "guayaba"]
codigos = ["mz01", "pr01", "gy01"]
precios = [2000, 2000, 5000]

inventario = {}

elementos = ["casa", 1, ["perro"], {"mz01": "manzana"}]

notas = {"nombre": "felipe", "edad": 32, "notas": [5, 3.5, 4, 0]}

matrix = [[2, 2], [3, 0], [4, 4]]

for codigo, fruta, precio in zip(codigos, frutas, precios):
    print(f"El código {codigo} corresponde a la fruta {fruta} que tiene precio {precio}")

for codigo in codigos:
    for fruta in frutas:
        inventario[codigo] = fruta
