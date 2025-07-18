import os
from domain.dataset_factory import DatasetFactory
from data.data_saver import Datasaver
from dotenv import load_dotenv

class AppLoader:
    def __init__(self):
        # Cargar variables de entorno
        load_dotenv()

        # Directorio de archivos
        self.files_dir = os.path.join(os.path.dirname(__file__), "files")
        
        # Definición de APIs (URL + key_path opcional)
        self.api_urls = [
            ("https://jsonplaceholder.typicode.com/users", None),
            # Podés agregar más APIs en el futuro
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
            dataset = DatasetFactory.create_dataset(api_url, key_path=key_path)

            if dataset is None:
                print(f"[WARNING] No se pudo crear dataset para API: {api_url}")
                continue

            try:
                dataset.cargar_datos()
                # Generamos un nombre de tabla simple a partir del nombre de la URL
                nombre_tabla = "api_" + api_url.split("/")[-1]
                self.data_saver.guardar_dataframe(dataset.datos, nombre_tabla)
            except Exception as e:
                print(f"[ERROR] Falló procesando API {api_url}: {e}")
