
---

### 🧠 **Ejercicio: Enriquecimiento de Datos de Ventas con Información de Clientes**

#### 📝 Descripción:

Ahora trabajarás con **dos archivos CSV**. El primero contiene datos de ventas de una tienda, y el segundo tiene información de los clientes que realizaron esas compras. Tu tarea será analizar las ventas, enriquecer los datos mediante una **unión (merge)** y extraer información relevante para el negocio.

#### 📁 Archivos:

1. `ventas.csv`

```csv
Fecha,Producto,Categoría,Cantidad,Precio Unitario,ID Cliente
2025-01-01,Camiseta,ropa,2,25.00,C001
2025-01-02,Zapatos,calzado,1,50.00,C002
2025-01-02,Pantalón,ropa,1,35.00,C003
2025-01-03,Sombrero,accesorios,3,10.00,C001
...
```

2. `clientes.csv`

```csv
ID Cliente,Nombre,Edad,Genero,País
C001,Ana,28,F,Colombia
C002,Luis,35,M,México
C003,Sofía,22,F,Argentina
...
```

---

### 🎯 Objetivos del ejercicio:

1. Leer ambos archivos CSV en DataFrames separados.
2. Mostrar las primeras 3 filas de cada DataFrame.
3. Unir los DataFrames usando la columna `ID Cliente` para enriquecer los datos de ventas.
4. Calcular el ingreso por venta (`Cantidad × Precio Unitario`) y agregarlo como una nueva columna llamada `Ingreso`.
5. Obtener el ingreso total de la tienda.
6. Mostrar la cantidad de ventas por país.
7. Determinar qué **grupo de edad** (por rangos: `<25`, `25–34`, `35+`) generó más ingresos.
8. Encontrar el producto más vendido **por género del cliente**.
9. Agrupar las ventas por mes y país, mostrando el total de ingresos por grupo.
10. Guardar el DataFrame resultante con la información completa en un archivo llamado `ventas_enriquecidas.csv`.

---

### 🛠 Requisitos:

* Python
* pandas

---

### 🧪 Pistas para los estudiantes:

* Usa `pd.read_csv()` para cargar los datos.
* Usa `pd.merge(df_ventas, df_clientes, on='ID Cliente')`.
* Usa `df['Ingreso'] = df['Cantidad'] * df['Precio Unitario']`.
* Usa `pd.cut()` para clasificar edades en grupos.
* Usa `groupby()` con múltiples columnas como `['Género', 'Producto']`.
* Usa `pd.to_datetime()` para extraer el mes de la fecha.

---
