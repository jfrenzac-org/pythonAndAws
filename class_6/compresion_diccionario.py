# Sin usar dictionary Comprehension

numeros = [1, 2, 3, 4]  # {2:4, 4:16}

cuadrados = []
for numero in numeros:
    if numero % 2 == 0:
        cuadrados.append(numero**2)

print("Cuadrados", cuadrados)

numeros_pares = []
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)


numeros_cuadrados = {}
for numero, cuadrado in zip(numeros_pares, cuadrados):
    if numero % 2 == 0:
        numeros_cuadrados[numero] = cuadrado

# Usando dictionary comprehension
# {key_expresion: value_expresion for item in iterable if condition}

numeros_cuadrados2 = {n: n**2 for n in numeros if n % 2 == 0}

print(numeros_cuadrados)
print(numeros_cuadrados2)
