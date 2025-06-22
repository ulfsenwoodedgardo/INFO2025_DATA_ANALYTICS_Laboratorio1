# Clase para carga de archivos .txt (tabulado)

import pandas as pd
from domain.dataset import Dataset

class DatasetTXTFile(Dataset):
    """
    Clase concreta para cargar y procesar archivos .txt (separado por tabulaciones)
    """

    def __init__(self, fuente):
        super().__init__(fuente)

    def cargar_datos(self):
        """
        Carga los datos desde un archivo .txt separado por tabulaciones.
        """
        try:
            df = pd.read_csv(self.fuente, sep="\t")
            self.datos = df

            if self.validar_datos():
                self.transformar_datos()

        except Exception as e:
            print(f"[DatasetTXTFile] Error cargando TXT: {e}")
