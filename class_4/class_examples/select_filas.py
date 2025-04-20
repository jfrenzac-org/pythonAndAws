import pandas as pd

datos = pd.read_csv("/root/pythonAndAws/class_4/class_examples/datos.csv")

# Obtener filas usando el método iloc
fila_1 = datos.iloc[0]

fila_1_5 = datos.iloc[0:6]

# Obtener Filas a partir de condiciones

# Fila del df a partir de una condición
nombre_cindy = datos[datos.first_name == "Cindy"]

# Filas del df a partir de más de una condición

# Utilizar el operador '|' para hacer uniones (or)
nombre_edad = datos[(datos.age < 30) | (datos.first_name == "Andrew")]

# Utilizar el operador '&' para hacer intersecciones (and)

nombre_y_edad = datos[(datos.age < 42) & (datos.first_name == "Patricia")]

print(nombre_y_edad)
