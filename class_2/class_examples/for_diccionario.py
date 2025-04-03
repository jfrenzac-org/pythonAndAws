# key -> keys()
# value - values()
# items()
# get()

frutas = {"m01z": "manzana", "p01r": "pera", "b01n": "banano"}

cantidades = {"m01z": 10, "p01r": 3, "b01n": 2}

# iter 1 ::: key == "m01z" value = "manzana"
# iter 2 ::: key == "p01r" value = "pera"
# iter 3 ::: key == "b01n" value = "banano"

for key, value in frutas.items():
    print(key, value)

for value in frutas.values():
    print(value)

for key in frutas.keys():
    print(key)

fruta = frutas.get("f", "no-existe")
fruta = frutas["m01z"]

if fruta == "no-existe":
    print("Esa fruta no está en el inventario")
else:
    print("la fruta es", fruta)
