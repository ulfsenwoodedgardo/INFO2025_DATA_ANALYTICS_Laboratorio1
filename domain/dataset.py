# Clase abstracta base para todos los datasets

from abc import ABC, abstractmethod

class Dataset(ABC):
    """
    Clase base abstracta para representar un dataset genérico.
    Todos los formatos (csv, xlsx, json, txt, api) heredarán de esta clase.
    """

    def __init__(self, fuente):
        """
        Constructor.

        Args:
            fuente (str): ruta del archivo o URL de la API.
        """
        self.__fuente = fuente
        self.__datos = None

    @property
    def datos(self):
        """
        Getter para los datos cargados.
        """
        return self.__datos

    @datos.setter
    def datos(self, value):
        """
        Setter para los datos. Aquí podrían agregarse validaciones adicionales.
        """
        self.__datos = value

    @property
    def fuente(self):
        """
        Getter para la fuente de los datos.
        """
        return self.__fuente

    @abstractmethod
    def cargar_datos(self):
        """
        Método abstracto que debe implementar cada subclase para cargar los datos.
        """
        pass

    def validar_datos(self):
        """
        Aplica validaciones mínimas:
        - Comprueba si hay datos
        - Informa si hay nulos
        - Informa si hay duplicados

        Returns:
            bool: True si pasa validaciones básicas.
        """
        if self.datos is None:
            raise ValueError("Datos no cargados")

        if self.datos.isnull().sum().sum() > 0:
            print("Datos faltantes detectados")

        if self.datos.duplicated().sum() > 0:
            print("Se detectaron filas duplicadas")

        return True

    def transformar_datos(self):
        """
        Aplica transformaciones estándar:
        - Renombra columnas a minúsculas y con _ en vez de espacios
        - Elimina duplicados
        - Limpia espacios en columnas tipo texto
        """
        if self.datos is not None:
            self.__datos.columns = self.datos.columns.str.lower().str.replace(" ", "_")
            self.__datos = self.datos.drop_duplicates()

            for col in self.datos.select_dtypes(include="object").columns:
                self.__datos.loc[:, col] = self.__datos[col].astype(str).str.strip()

            print("Transformaciones han sido aplicadas")
        else:
            print("No hay datos para transformar")

    def mostrar_resumen(self):
        """
        Muestra un resumen estadístico de los datos (describe).
        """
        print(self.datos.describe(include='all') if self.datos is not None else "No hay datos")
