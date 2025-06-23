import requests
import pandas as pd
from domain.dataset import Dataset

class DatasetAPI(Dataset):
    def __init__(self, fuente, key_path=None):
        """
        DatasetAPI permite cargar datos desde APIs REST (JSON).
        
        :param fuente: URL de la API
        :param key_path: Ruta de claves para acceder al array de datos en el JSON (opcional)
                         Ejemplo: "provincias" o "results.items"
        """
        super().__init__(fuente)
        self.key_path = key_path

    def _extract_data_by_key_path(self, data, key_path):
        """
        Extrae datos de un JSON anidado usando una key_path tipo 'a.b.c'.
        Lanza KeyError si alguna clave no existe.

        :param data: El JSON completo recibido
        :param key_path: Ruta de claves separadas por '.'
        :return: Subestructura de datos obtenida
        """
        keys = key_path.split('.')
        for k in keys:
            if isinstance(data, dict) and k in data:
                data = data[k]
            else:
                raise KeyError(
                    f"Key path '{key_path}' falló en '{k}'. "
                    f"Claves disponibles en este nivel: {list(data.keys()) if isinstance(data, dict) else 'N/A'}"
                )
        return data

    def cargar_datos(self):
        """
        Carga y procesa datos desde la API.
        - Realiza GET a la URL.
        - Extrae datos por key_path si es necesario.
        - Convierte el resultado a DataFrame.
        - Aplica validaciones y transformaciones.
        """
        try:
            response = requests.get(self.fuente)

            if response.status_code == 200:
                data = response.json()

                # Si se especificó un key_path, intentar extraer la sección correspondiente
                if self.key_path:
                    try:
                        data = self._extract_data_by_key_path(data, self.key_path)
                    except KeyError as e:
                        print(f"[ERROR] {e}")
                        return

                # Verificar tipo de datos extraídos
                if not isinstance(data, (list, dict)):
                    print(f"[ERROR] Los datos extraídos de la API no son una lista ni un diccionario. Tipo: {type(data)}")
                    print(f"Valor obtenido: {data}")
                    return

                # Normalizar datos a DataFrame
                df = pd.json_normalize(data)

                # Convertir listas a string para compatibilidad
                df = self._convertir_listas_a_string(df)

                # Guardar en atributo 'datos'
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
        """
        Convierte columnas que contienen listas en strings.
        
        :param df: DataFrame a procesar
        :return: DataFrame transformado
        """
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
