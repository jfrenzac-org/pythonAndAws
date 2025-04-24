"""
Capitalizar solo las palabras que tengan más de 4 letras
De una lista de palabras, devolver otra con las que tienen más de 4 letras y estén capitalizadas.
Entrada: ["sol", "computadora", "mesa", "ventana"]
Salida esperada: ["Computadora", "Ventana"]
Usa filter(), map() y lambda.
"""
palabras = ["piso", "cable", "computador", "control", "televisor", "cama"]

capitalizadas = list(map(lambda palabra: palabra.capitalize(),
                         filter(lambda palabra: len(palabra)> 4, palabras)))

## Con la función filter se seleccionan las palabras que tienen más de 4 letras
## Con la función map se capitalizan las palabras filtradas.

print(capitalizadas)

