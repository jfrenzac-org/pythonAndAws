import pandas as pd
from faker import Faker
import random
from datetime import datetime


class CrearDatos:
    def __init__(self, cantidad_filas: int):
        self.fake = Faker()
        self.cantidad_filas = cantidad_filas
        self.data = []

    def crear_datos_ficticios(self, especificaciones: dict):
        """
        Genera datos ficticios basados en las especificaciones del diccionario.
        El diccionario debe tener la estructura:
        {
            "columna": ("tipo", [valores] o rango)
        }
        Tipos admitidos: 'faker', 'random_choice', 'random_int', 'random_float', 'fecha'
        """
        for _ in range(self.cantidad_filas):
            fila = {}
            for columna, (tipo, valor) in especificaciones.items():
                if tipo == "faker":
                    fila[columna] = getattr(self.fake, valor)()
                elif tipo == "random_choice":
                    fila[columna] = random.choice(valor)
                elif tipo == "random_int":
                    fila[columna] = random.randint(*valor)
                elif tipo == "random_float":
                    fila[columna] = round(random.uniform(*valor), 2)
                elif tipo == "fecha":
                    start_date = datetime.strptime(valor[0], "%Y-%m-%d").date()
                    end_date = datetime.strptime(valor[1], "%Y-%m-%d").date()
                    fila[columna] = self.fake.date_between(start_date=start_date, end_date=end_date)

                else:
                    raise ValueError(f"Tipo de dato no soportado: {tipo}")
            self.data.append(fila)

    def crear_csv_file(self, nombre_archivo: str):
        df = pd.DataFrame(self.data)
        df.to_csv(nombre_archivo, index=False)


# Ejemplo de uso con datos de ventas
if __name__ == "__main__":
    ventas_spec = {
        "Fecha": ("fecha", ("2025-01-01", "2025-12-31")),
        "Producto": (
            "random_choice",
            [
                "Camiseta",
                "Pantalón",
                "Zapatos",
                "Sandalias",
                "Sombrero",
                "Bolso",
                "Bufanda",
                "Chaqueta",
            ],
        ),
        "Categoría": (
            "random_choice",
            [
                "ropa",
                "ropa",
                "calzado",
                "calzado",
                "accesorios",
                "accesorios",
                "accesorios",
                "ropa",
            ],
        ),
        "Cantidad": ("random_int", (1, 5)),
        "Precio Unitario": ("random_float", (10.0, 100.0)),
    }

    generador = CrearDatos(cantidad_filas=1000)  # Solo se debe modificar el número de filas
    generador.crear_datos_ficticios(
        ventas_spec
    )  # Solo modificar 'ventas_spec' si el nombre del diccionario cambia
    generador.crear_csv_file("datos/ventas.csv")  # el path siempre será "datos/nombre_archivo.csv"
