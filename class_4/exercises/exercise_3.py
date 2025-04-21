"""
Obtener la longitud de cada palabra

De una lista de palabras, obtener una lista con la longitud de cada una.
Entrada: ["hola", "mundo", "python"]
Salida esperada: [4, 5, 6]
Usa map()
"""

palabras = ["hola", "mundo", "python"]

longitud_palabras = map(lambda x: len(x), palabras)

print(list(longitud_palabras))
