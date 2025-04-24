"""
Filtrar palabras que comienzan con vocal
Filtra de una lista las palabras que comienzan con una vocal.
Entrada: ["uva", "banana", "naranja", "arándano", "melón"]
Salida esperada: ["uva", "arándano"]
Usa filter() con lambda.
"""

palabras = ["Panes", "Azúcar", "Limón", "Ostras", "ají", "pepino", "Eneldo", "uchuvas"]
vocales = ('a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'ü')

## solamente con la función filter con lambda se obtiene el resultado.

comienzan_vocal = list(filter(lambda palabra:
palabra.lower().startswith(vocales), palabras))

print(comienzan_vocal)