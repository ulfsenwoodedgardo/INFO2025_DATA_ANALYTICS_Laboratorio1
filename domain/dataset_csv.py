# Clase para cargar datos desde archivos CSV

import pandas as pd
from domain.dataset import Dataset

class DatasetCSVFile(Dataset):
    """
    Clase para representar un dataset proveniente de un archivo CSV.
    """

    def __init__(self, fuente):
        """
        Constructor.

        Args:
            fuente (str): Ruta del archivo CSV.
        """
        super().__init__(fuente)

    def cargar_datos(self):
        """
        Carga los datos desde el archivo CSV.
        Aplica validación y transformación.
        """
        try:
            df = pd.read_csv(self.fuente)
            self.datos = df

            if self.validar_datos():
                self.transformar_datos()

        except Exception as e:
            print(f"[DatasetCSVFile] Error cargando CSV: {e}")
