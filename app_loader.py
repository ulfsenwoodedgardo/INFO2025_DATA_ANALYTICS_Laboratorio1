import os
from domain.dataset_factory import DatasetFactory
from data.data_saver import Datasaver

class AppLoader:
    def __init__(self):
        self.data_dir = os.path.join(os.path.dirname(__file__), "files")
        self.db = Datasaver()
        self.reporte = []

    def run(self):
        for filename in os.listdir(self.data_dir):
            filepath = os.path.join(self.data_dir, filename)
            try:
                dataset = DatasetFactory.crear_dataset(filepath)
                dataset.cargar_datos()
                dataset.mostrar_resumen()
                self.db.guardar_dataframe(dataset.datos, os.path.splitext(filename)[0])
                self.reporte.append((filename, "✔️ OK"))
            except Exception as e:
                self.reporte.append((filename, f"❌ Falló: {e}"))

        print("\n== 📝 Reporte Final ==")
        for archivo, resultado in self.reporte:
            print(f"{archivo}: {resultado}")
