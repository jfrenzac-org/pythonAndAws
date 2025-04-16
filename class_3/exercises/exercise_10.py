"""
Ejercicio 10: Capitalizar frase

Enunciado:

Crea una función que reciba una frase y devuelva la misma frase con la primera
letra de cada palabra en mayúscula (como en los títulos de libros).

"""


def mayusculas_en_frase(texto: str) -> str:
    palabras = texto.strip().split()
    capitalizadas = [palabra.capitalize() for palabra in palabras]
    return " ".join(capitalizadas)


if __name__ == "__main__":
    texto = "this is the text that will serve as input"
    print(mayusculas_en_frase(texto))
