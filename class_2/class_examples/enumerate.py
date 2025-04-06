# enumerate()
frutas = ["manzana", "pera", "banano"]

fruta_idx = list(enumerate(frutas))

for i, fruta in enumerate(frutas, start=1):
    print(f"La fruta número '{i}_producto_exito_poblado' es: {fruta}")

# i = 0
# for fruta in frutas:
#     if i == 0:
#         i = 1
#     print(f"La fruta número {i} es: {fruta}")
#     i = i + 1
