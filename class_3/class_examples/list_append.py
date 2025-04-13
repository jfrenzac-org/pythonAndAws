"""
list.append()
list.extend()
list.sort()
len()
"""

# list.append()

frutas = ["Manzana", "Mango", "Pera", "Banano", "Mandarina", "Kiwi"]

frutas_con_m = []

for fruta in frutas:
    fruta_en_minuscula = fruta.lower()
    comienza_con = fruta_en_minuscula.startswith("m")
    if comienza_con:
        frutas_con_m.append(fruta)

print(frutas_con_m)  # ["Manzana", "Mango", "Mandarina"]
