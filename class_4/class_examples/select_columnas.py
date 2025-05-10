"""
snake_case :: Palabras todas en minúscula y si existe más de una palabra,
deben estar separadas por guion bajo

first_name

"""

import pandas as pd

datos = pd.read_csv("datos/datos.csv")

columna_1 = datos["first_name"]

new_df = datos[["first_name", "age"]]

columna_1 = datos.first_name

print(columna_1)
