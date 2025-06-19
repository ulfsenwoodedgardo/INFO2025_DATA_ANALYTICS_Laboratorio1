import pandas as pd
from domain.dataset import Dataset

class DatasetCSVFile(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)

    def cargar_datos(self):
        try:
            df = pd.read_csv(self.fuente)
            self.datos = df
            if self.validar_datos():
                self.transformar_datos()
        except Exception as e:
            print(f"[DatasetCSVFile] Error cargando CSV: {e}")
