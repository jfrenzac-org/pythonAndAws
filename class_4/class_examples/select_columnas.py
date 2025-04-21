"""
snake_case :: Palabras todas en minúscula y si existe más de una palabra,
deben estar separadas por guion bajo

first_name

"""

import pandas as pd

datos = pd.read_csv("/root/pythonAndAws/class_4/class_examples/datos.csv")

columna_1 = datos["first name"]

new_df = datos[["first name", "age"]]

columna_1 = datos.first_name

print(columna_1)
