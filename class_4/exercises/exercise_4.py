"""
Filtrar palabras que comienzan con vocal
Filtra de una lista las palabras que comienzan con una vocal.
Entrada: ["uva", "banana", "naranja", "arándano", "melón"]
Salida esperada: ["uva", "arándano"]
Usa filter() con lambda.
"""

frutas = ["uva", "banana", "naranja", "arándano", "melón"]

frutas_con_vocal = filter(lambda x: x[0] in ["a", "e", "i", "o", "u"], frutas)

print(list(frutas_con_vocal))
