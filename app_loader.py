# Clase principal que gestiona la carga de archivos y APIs, y guarda los datos en la base

import os
from domain.dataset_factory import DatasetFactory
from data.data_saver import Datasaver
from dotenv import load_dotenv

class AppLoader:
    def __init__(self):
        # Cargar variables de entorno (.env)
        load_dotenv()

        # Directorio donde se encuentran los archivos a procesar
        self.files_dir = os.path.join(os.path.dirname(__file__), "files")
        
        # URLs de APIs que se quieren procesar
        self.api_urls = [
            "https://apis.datos.gob.ar/georef/api/provincias"
            # Podés agregar más APIs si querés
        ]

        # Instancia de clase para guardar en base de datos
        self.data_saver = Datasaver()

    def run(self):
        """
        Método principal de ejecución: procesa archivos y APIs
        """
        self._procesar_archivos()
        self._procesar_apis()

    def _procesar_archivos(self):
        """
        Procesa todos los archivos en la carpeta 'files'
        """
        print("\n=== PROCESANDO ARCHIVOS ===")
        
        for filename in os.listdir(self.files_dir):
            filepath = os.path.join(self.files_dir, filename)

            # Ignorar subdirectorios
            if not os.path.isfile(filepath):
                continue  

            # Crear dataset adecuado según la extensión
            dataset = DatasetFactory.create_dataset(filepath)

            if dataset is None:
                print(f"[WARNING] Tipo de archivo no soportado: {filename}")
                continue

            try:
                # Cargar datos y guardar en base
                dataset.cargar_datos()
                self.data_saver.guardar_dataframe(dataset.datos, os.path.splitext(filename)[0])
            except Exception as e:
                print(f"[ERROR] Falló procesando {filename}: {e}")

    def _procesar_apis(self):
        """
        Procesa las APIs definidas en 'api_urls'
        """
        print("\n=== PROCESANDO APIs ===")

        for api_url in self.api_urls:
            dataset = DatasetFactory.create_dataset(api_url)

            if dataset is None:
                print(f"[WARNING] No se pudo crear dataset para API: {api_url}")
                continue

            try:
                # Cargar datos y guardar en base
                dataset.cargar_datos()
                nombre_tabla = "api_" + api_url.split("/")[-1]
                self.data_saver.guardar_dataframe(dataset.datos, nombre_tabla)
            except Exception as e:
                print(f"[ERROR] Falló procesando API {api_url}: {e}")
