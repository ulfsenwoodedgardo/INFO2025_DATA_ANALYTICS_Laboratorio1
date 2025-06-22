import requests
import pandas as pd
from domain.dataset import Dataset

class DatasetAPI(Dataset):
    def __init__(self, fuente, key_path=None):
        """
        :param fuente: URL de la API
        :param key_path: clave o ruta de claves para acceder al array de datos en el JSON
                         Ejemplo: "provincias" o "results.items"
        """
        super().__init__(fuente)
        self.key_path = key_path

    def cargar_datos(self):
        try:
            response = requests.get(self.fuente)
            if response.status_code == 200:
                data = response.json()

                # Si se especificó un key_path (para APIs que tienen la data adentro)
                if self.key_path:
                    keys = self.key_path.split('.')
                    for k in keys:
                        data = data.get(k, {})
                    # Puede ser dict vacío si no se encuentra la clave

                # Normalizar a DataFrame
                if isinstance(data, list):
                    df = pd.json_normalize(data)
                elif isinstance(data, dict):
                    df = pd.json_normalize(data)
                else:
                    raise ValueError("Formato de datos inesperado")

                # Convertir listas a string
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
        def es_lista(x):
            return isinstance(x, list)

        def lista_a_string(x):
            if isinstance(x, list):
                return ', '.join(map(str, x))
            return x

        for col in df.columns:
            if df[col].apply(es_lista).any():
                df[col] = df[col].apply(lista_a_string)

        return df
