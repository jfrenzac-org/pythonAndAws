"""
Análisis de Ventas

1. Leer el archivo CSV en un DataFrame.
2. Mostrar las primeras 5 filas.
3. Obtener el número total de ventas realizadas (filas del archivo).
4. Calcular el ingreso total por cada venta (Cantidad X Precio Unitario)
    y agregarlo como una nueva columna llamada Ingreso.
5. Obtener el ingreso total de la tienda.
6. Mostrar las ventas totales por categoría.
7. Encontrar el producto más vendido (en términos de cantidad total).
8. Mostrar las ventas mensuales totales (agrupando por mes).
9. Guardar el DataFrame con la nueva columna en un archivo llamado
    ventas_con_ingresos.csv.

"""

import pandas as pd

# Punto 1

ventas = pd.read_csv("datos/ventas.csv")

# Punto 2
print(ventas.head(5))

# Punto 3

total_ventas = sum(ventas.Cantidad)
print(f"Las ventas totales fueron: USD {total_ventas}")

# Punto 4

ventas["Ingreso"] = ventas.Cantidad * ventas["Precio Unitario"]

print(ventas)

# Punto 5

ingreso_total = sum(ventas.Ingreso)

print(f"El ingreso total de la tienda fue: USD {ingreso_total}")

# Punto 6

ventas_por_categoria = ventas.groupby(ventas.Categoría)["Precio Unitario"].sum()

print(ventas_por_categoria)

# Punto 7

producto_mas_vendido = ventas.groupby("Categoría")["Cantidad"].sum().sort_values(ascending=False)

print(producto_mas_vendido)

# Punto 8
# Asegúrate de que 'Fecha' sea datetime
ventas["Fecha"] = pd.to_datetime(ventas["Fecha"])

# Extraer nombre del mes abreviado
ventas["Mes"] = ventas["Fecha"].dt.strftime("%b")

# Agrupar por nombre de mes y sumar ingresos
ventas_totales_mes = ventas.groupby("Mes")["Ingreso"].sum()

# (Opcional) Ordenar los meses cronológicamente
orden_meses = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
ventas_totales_mes = ventas_totales_mes.reindex(orden_meses)

print(ventas_totales_mes)
# Punto 9
ventas.to_csv("datos/ventas_con_ingresos.csv", index=False)
