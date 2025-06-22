# Clase encargada de guardar DataFrames en una base de datos relacional usando SQLAlchemy

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from decouple import config

class Datasaver:
    """
    Clase que encapsula la lógica para persistir datos en una base de datos.
    """

    def __init__(self):
        """
        Constructor: crea la conexión a la base de datos usando las variables de entorno.
        """
        # Leer configuración desde .env
        user = config('DB_USER')
        password = config('DB_PASSWORD')
        host = config('DB_HOST')
        database = config('DB_NAME')
        port = config('DB_PORT')

        # Crear URL de conexión compatible con SQLAlchemy
        url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        self.engine = create_engine(url)

    def guardar_dataframe(self, df, nombre_tabla):
        """
        Guarda un DataFrame en la base de datos en una tabla con el nombre indicado.

        Args:
            df (DataFrame): datos a guardar.
            nombre_tabla (str): nombre de la tabla destino.
        """
        if df is None:
            print(f"No se puede guardar: datos vacíos para {nombre_tabla}")
            return

        if not isinstance(df, pd.DataFrame):
            print(f"Tipo inválido: se esperaba un DataFrame, se recibió {type(df)}")
            return

        try:
            df.to_sql(nombre_tabla, con=self.engine, if_exists='replace', index=False)
            print(f"Datos guardados en tabla: {nombre_tabla}")

        except SQLAlchemyError as e:
            print(f"Error guardando datos: {e}")
