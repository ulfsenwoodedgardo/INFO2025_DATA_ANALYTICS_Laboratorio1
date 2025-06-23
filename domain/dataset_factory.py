import os
from domain.dataset_csv import DatasetCSVFile
from domain.dataset_excel import DatasetExcelFile
from domain.dataset_json import DatasetJSONFile
from domain.dataset_txt import DatasetTXTFile
from domain.dataset_api import DatasetAPI

class DatasetFactory:
    @staticmethod
    def create_dataset(file_or_url, key_path=None):
        # Si es URL (API), crear DatasetAPI
        if file_or_url.startswith("http://") or file_or_url.startswith("https://"):
            return DatasetAPI(file_or_url, key_path=key_path)

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
