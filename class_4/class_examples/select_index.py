import pandas as pd
datos=pd.read_csv('data.csv')
# print(datos.iloc[0])
# print(datos.iloc[5:6])
#Con esta línea se busca en el dataframe "datos", la columna que se llama "name" y presenta las filas que tiene el nombre "Cindy"
print(datos[datos.name=="Cindy"])
# "|" es un operador lógico que significa "o". En este caso, se está buscando filas donde la edad sea menor de 30 o el nombre sea "Cindy".
print(datos[(datos.age<30)|(datos.name=="Cindy")])
# "&" es un operador lógico que significa "y". En este caso, se está buscando filas donde la edad sea menor de 30 y el nombre sea "Cindy".
print(datos[(datos.age<30)&(datos.name=="Cindy")])