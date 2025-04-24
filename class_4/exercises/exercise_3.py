"""
Obtener la longitud de cada palabra

De una lista de palabras, obtener una lista con la longitud de cada una.
Entrada: ["hola", "mundo", "python"]
Salida esperada: [4, 5, 6]
Usa map()
"""
palabras = ["estas", "son", "las", "palabras", "en", "ejercicio"]

## Con una sola linea de código usando la función map y el método len(), se obtiene el resultado.

resultado = list(map(len, palabras))
print(resultado)