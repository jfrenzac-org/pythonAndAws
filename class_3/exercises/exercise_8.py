"""
Ejercicio 8: Eliminar espacios sobrantes

Enunciado:

Escribe una función que reciba un string y devuelva ese mismo string sin los
espacios en blanco al principio ni al final. Usa el método strip().
"""


def elimina_espacios(texto: str) -> str:
    return texto.strip()


if __name__ == "__main__":
    texto = "     This has blank spaces     "
    print(elimina_espacios(texto))
