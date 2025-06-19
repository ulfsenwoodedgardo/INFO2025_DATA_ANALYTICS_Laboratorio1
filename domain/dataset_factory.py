import os
from domain.dataset_csv import DatasetCSVFile
from domain.dataset_excel import DatasetExcelFile
from domain.dataset_json import DatasetJSONFile
from domain.dataset_txt import DatasetTXTFile

class DatasetFactory:
    @staticmethod
    def crear_dataset(filepath):
        extension = os.path.splitext(filepath)[1].lower()

        if extension == '.csv':
            return DatasetCSVFile(filepath)
        elif extension == '.xlsx':
            return DatasetExcelFile(filepath)
        elif extension == '.json':
            return DatasetJSONFile(filepath)
        elif extension == '.txt':
            return DatasetTXTFile(filepath)
        else:
            print(f"[DatasetFactory] Formato no soportado: {extension}")
            return None

