
---

### 🧠 **Ejercicio: Análisis de Ventas de una Tienda**

#### 📝 Descripción:

Tienes un archivo CSV con datos de ventas de una tienda durante el año. Cada fila representa una venta individual.

#### 📁 Archivo: `ventas.csv`

```csv
Fecha,Producto,Categoría,Cantidad,Precio Unitario
2025-01-01,Camiseta,ropa,2,25.00
2025-01-02,Zapatos,calzado,1,50.00
2025-01-02,Pantalón,ropa,1,35.00
2025-01-03,Sombrero,accesorios,3,10.00
...
```

#### 🎯 Objetivos del ejercicio:

1. **Leer** el archivo CSV en un DataFrame.
2. Mostrar las **primeras 5 filas**.
3. Obtener el número total de **ventas realizadas** (filas del archivo).
4. Calcular el ingreso total por cada venta (Cantidad × Precio Unitario) y agregarlo como una nueva columna llamada `Ingreso`.
5. Obtener el **ingreso total de la tienda**.
6. Mostrar las **ventas totales por categoría**.
7. Encontrar el **producto más vendido** (en términos de cantidad total).
8. Mostrar las **ventas mensuales totales** (agrupando por mes).
9. Guardar el DataFrame con la nueva columna en un archivo llamado `ventas_con_ingresos.csv`.

---

### 🛠 Requisitos:

* Python
* pandas

---

### 🧪 Pistas para los estudiantes:

* Usa `pd.read_csv()` para leer el archivo.
* Usa `df['Ingreso'] = df['Cantidad'] * df['Precio Unitario']`.
* Usa `groupby()` para agrupar por categoría o mes.
* Usa `to_datetime()` para convertir la columna `Fecha` y extraer el mes.
