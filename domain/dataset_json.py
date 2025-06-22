# Clase para carga de archivos .json

import pandas as pd
from domain.dataset import Dataset

class DatasetJSONFile(Dataset):
    """
    DatasetJSONFile:
    Clase que carga archivos .json en un DataFrame
    Hereda de la clase base Dataset
    """

    def __init__(self, fuente):
        # Llamada al constructor de la clase base
        super().__init__(fuente)

    def cargar_datos(self):
        """
        Carga los datos del archivo .json en el atributo 'datos'.
        Aplica validación y transformación
        """
        try:
            # Carga el JSON en un DataFrame
            df = pd.read_json(self.fuente)
            self.datos = df

            # Validación y transformación
            if self.validar_datos():
                self.transformar_datos()

        except Exception as e:
            print(f"[DatasetJSONFile] Error cargando JSON: {e}")
