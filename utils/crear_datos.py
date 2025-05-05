import pandas as pd
from faker import Faker
import random
from datetime import datetime


class CrearDatos:
    def __init__(self, cantidad_filas: int):
        self.fake = Faker()
        self.cantidad_filas = cantidad_filas
        self.data = []

    def crear_datos_ficticios(self, especificaciones: dict, mapas_dependencias: dict = None):
        """
        especificaciones: diccionario con estructura:
            {
                "columna": ("tipo", valores)
            }
        mapas_dependencias: diccionario opcional con estructura:
            {
                "columna_dependiente": {"valor_origen": "valor_dependiente", ...}
            }
        """
        for i in range(self.cantidad_filas):
            fila = {}
            for columna, (tipo, valor) in especificaciones.items():
                if tipo == "consecutivo":
                    fila[columna] = i
                elif tipo == "faker":
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

            # aplicar dependencias después de crear la fila base
            if mapas_dependencias:
                for dependiente, mapping in mapas_dependencias.items():
                    origen = next((k for k in especificaciones if k in mapping), None)
                    if origen and origen in fila:
                        fila[dependiente] = mapping[fila[origen]]

            self.data.append(fila)

    def crear_csv_file(self, nombre_archivo: str):
        df = pd.DataFrame(self.data)
        df.to_csv(nombre_archivo, index=False)


if __name__ == "__main__":

    clientes_spec = {
        "ID": ("consecutivo", None),
        "Nombre": ("faker", "first_name"),
        "Edad": ("random_int", (18, 70)),
        "Genero": ("random_choice", ["Masculino", "Femenino"]),
        "Pais": ("faker", "country"),
    }

    generador = CrearDatos(cantidad_filas=1000)
    generador.crear_datos_ficticios(clientes_spec)
    generador.crear_csv_file("datos/clientes.csv")
