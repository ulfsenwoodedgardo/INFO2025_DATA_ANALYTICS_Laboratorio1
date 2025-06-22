# Fábrica de objetos Dataset según el tipo de archivo o API

import os
from domain.dataset_csv import DatasetCSVFile
from domain.dataset_excel import DatasetExcelFile
from domain.dataset_json import DatasetJSONFile
from domain.dataset_txt import DatasetTXTFile
from domain.dataset_api import DatasetAPI

class DatasetFactory:
    """
    Fábrica de objetos Dataset.
    Decide qué clase Dataset instanciar en función de:
    - extensión de archivo (csv, xlsx, json, txt)
    - o bien, si es una URL (para API)
    """

    @staticmethod
    def create_dataset(file_or_url):
        """
        Devuelve una instancia de la clase Dataset correspondiente.

        :param file_or_url: path de archivo o URL de API
        :return: instancia de Dataset o None
        """
        # Si es URL de API
        if file_or_url.startswith("http://") or file_or_url.startswith("https://"):
            return DatasetAPI(file_or_url)

        # Si es archivo local, detectar extensión
        extension = os.path.splitext(file_or_url)[1].lower()

        if extension == '.csv':
            return DatasetCSVFile(file_or_url)
        elif extension == '.xlsx':
            return DatasetExcelFile(file_or_url)
        elif extension == '.json':
            return DatasetJSONFile(file_or_url)
        elif extension == '.txt':
            return DatasetTXTFile(file_or_url)
        else:
            print(f"[DatasetFactory] Formato no soportado: {extension}")
            return None
