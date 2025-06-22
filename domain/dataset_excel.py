# Clase para cargar datos desde archivos Excel (.xlsx)

import pandas as pd
from domain.dataset import Dataset

class DatasetExcelFile(Dataset):
    """
    Clase para representar un dataset proveniente de un archivo Excel.
    """

    def __init__(self, fuente):
        """
        Constructor.

        Args:
            fuente (str): Ruta del archivo Excel.
        """
        super().__init__(fuente)

    def cargar_datos(self):
        """
        Carga los datos desde el archivo Excel.
        Aplica validación y transformación.
        """
        try:
            df = pd.read_excel(self.fuente)
            self.datos = df

            if self.validar_datos():
                self.transformar_datos()

        except Exception as e:
            print(f"[DatasetExcelFile] Error cargando Excel: {e}")
