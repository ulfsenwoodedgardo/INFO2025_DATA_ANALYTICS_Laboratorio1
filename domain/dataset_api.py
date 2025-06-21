import requests
import pandas as pd
from domain.dataset import Dataset

class DatasetAPI(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)

    def cargar_datos(self):
        try:
            response = requests.get(self.fuente)
            if response.status_code == 200:
                # Normalizar el JSON
                df = pd.json_normalize(response.json())

                # Convertir columnas tipo lista a string
                df = self._convertir_listas_a_string(df)

                # Guardar datos
                self.datos = df

                # Validar y transformar
                if self.validar_datos():
                    self.transformar_datos()

                print(f"[OK] API cargada desde: {self.fuente}")

            else:
                print(f"[ERROR] API respondió con status: {response.status_code}")

        except Exception as e:
            print(f"[ERROR] Error al cargar API: {e}")

    def _convertir_listas_a_string(self, df):
        # Verificar si un valor es una lista
        def es_lista(x):
            return isinstance(x, list)

        # Transformar listas a string
        def lista_a_string(x):
            if isinstance(x, list):
                return ', '.join(map(str, x))
            return x

        for col in df.columns:
            if df[col].apply(es_lista).any():
                df[col] = df[col].apply(lista_a_string)

        return df
