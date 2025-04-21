"""
Capitalizar solo las palabras que tengan más de 4 letras
De una lista de palabras, devolver otra con las que tienen más de 4 letras y estén capitalizadas.
Entrada: ["sol", "computadora", "mesa", "ventana"]
Salida esperada: ["Computadora", "Ventana"]
Usa filter(), map() y lambda.
"""

palabras = ["sol", "computadora", "mesa", "ventana"]

palabras_4_letras = map(lambda x: x.capitalize(), filter(lambda x: len(x) > 4, palabras))

print(list(palabras_4_letras))
