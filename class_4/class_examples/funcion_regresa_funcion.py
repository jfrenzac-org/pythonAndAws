"""
Función de orden superior, Función que retorna función
"""


def crear_multiplicador(factor):
    def multiplicar(x):
        return x * factor

    return multiplicar


por_dos = crear_multiplicador(2)
por_cinco = crear_multiplicador(5)

print(por_dos(10))  # 20
print(por_cinco(10))  # 50
