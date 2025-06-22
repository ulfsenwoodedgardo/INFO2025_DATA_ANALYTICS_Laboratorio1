import os
from domain.dataset_factory import DatasetFactory
from domain.dataset_api import DatasetAPI
from data.data_saver import Datasaver
from dotenv import load_dotenv

class AppLoader:
    def __init__(self):
        # Cargar variables de entorno
        load_dotenv()

        # Directorio de archivos
        self.files_dir = os.path.join(os.path.dirname(__file__), "files")
        
        # Definición de APIs a cargar
        # Cada entrada es una tupla: (url, key_path)
        self.api_urls = [
            ("https://apis.datos.gob.ar/georef/api/provincias", "provincias"),
            # ("https://miapi.com/data", "result.items"),  # etc...
            ]

        # Instancia de la clase de guardado
        self.data_saver = Datasaver()

    def run(self):
        self._procesar_archivos()
        self._procesar_apis()

    def _procesar_archivos(self):
        print("\n=== PROCESANDO ARCHIVOS ===")
        
        for filename in os.listdir(self.files_dir):
            filepath = os.path.join(self.files_dir, filename)

            if not os.path.isfile(filepath):
                continue  # Ignorar subdirectorios

            # Crear dataset
            dataset = DatasetFactory.create_dataset(filepath)

            if dataset is None:
                print(f"[WARNING] Tipo de archivo no soportado: {filename}")
                continue

            try:
                dataset.cargar_datos()
                self.data_saver.guardar_dataframe(dataset.datos, os.path.splitext(filename)[0])
            except Exception as e:
                print(f"[ERROR] Falló procesando {filename}: {e}")

    def _procesar_apis(self):
        print("\n=== PROCESANDO APIs ===")

        for api_url, key_path in self.api_urls:
            # Crear dataset API con key_path
            dataset = DatasetAPI(api_url, key_path=key_path)

            try:
                dataset.cargar_datos()
                # Generar nombre de tabla simple
                nombre_tabla = "api_" + api_url.split("/")[-1]
                self.data_saver.guardar_dataframe(dataset.datos, nombre_tabla)
            except Exception as e:
                print(f"[ERROR] Falló procesando API {api_url}: {e}")
