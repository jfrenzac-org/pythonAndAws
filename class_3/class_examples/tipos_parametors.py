# Tipos de parámetros

# Posición
# Llave - Key
# Parametros por defecto


# Parámetros de tipo posición
def crear_usuario(apellido, nombre):
    usuario = apellido + nombre + "01"
    return usuario


print(crear_usuario("renza", "felipe"))


# Parámentros de tipo llave
def crear_usuario(apellido, nombre):
    usuario = apellido + nombre + "01"
    return usuario


print(crear_usuario(nombre="felipe", apellido="renza"))


# Parámetro por defecto
def crear_usuario(apellido, nombre, codigo="01"):
    usuario = apellido + nombre + codigo
    return usuario


print(crear_usuario(nombre="felipe", apellido="renza"))


"""
La ejecución de esta función fallará pues
si la definición tiene 'n' parámentros y ninguno es 
un parámetro por defecto, al momento de usarla debo
utilizar 'n' argumentos
"""


def suma(n1, n2):
    return n1 + n2


print(suma(2))
