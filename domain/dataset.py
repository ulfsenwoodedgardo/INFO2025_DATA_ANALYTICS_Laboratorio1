from abc import ABC, abstractmethod

class Dataset(ABC): 
    def __init__(self, fuente):
        self.__fuente = fuente
        self.__datos = None

    @property
    def datos(self):
        return self.__datos

    @datos.setter
    def datos(self, value):
        self.__datos = value

    @property
    def fuente(self):
        return self.__fuente

    @abstractmethod
    def cargar_datos(self):
        pass

    def validar_datos(self):
        if self.datos is None:
            raise ValueError("Datos no cargados")
        if self.datos.isnull().sum().sum() > 0:
            print("Datos faltantes detectados")
        if self.datos.duplicated().sum() > 0:
            print("Se detectaron filas duplicadas")
        return True

    def transformar_datos(self):
        if self.datos is not None:
            self.__datos.columns = self.datos.columns.str.lower().str.replace(" ", "_")
            self.__datos = self.datos.drop_duplicates()
            for col in self.datos.select_dtypes(include="object").columns:
                self.__datos[col] = self.datos[col].astype(str).str.strip()
            print("Transformaciones han sido aplicadas")
        else:
            print("No hay datos para transformar")

    def validar_esquema(self, esquema):
        """
        esquema: dict con la forma:
        {
            "columna1": {"tipo": "float64", "obligatorio": True},
            "columna2": {"tipo": "object", "obligatorio": False},
            ...
        }
        """
        if self.datos is None:
            raise ValueError("Datos no cargados, no se puede validar esquema")

        print("\nValidando esquema...")

        for columna, reglas in esquema.items():
            if columna not in self.datos.columns:
                print(f"[WARNING] Falta columna esperada: {columna}")
                continue

            tipo_esperado = reglas.get("tipo")
            obligatorio = reglas.get("obligatorio", False)

            # Validar tipo
            tipo_actual = str(self.datos[columna].dtype)
            if tipo_esperado and tipo_actual != tipo_esperado:
                print(f"[WARNING] Tipo incorrecto en columna '{columna}': esperado {tipo_esperado}, encontrado {tipo_actual}")

            # Validar valores nulos en campos obligatorios
            if obligatorio:
                nulos = self.datos[columna].isnull().sum()
                if nulos > 0:
                    print(f"[WARNING] {nulos} valores nulos en columna obligatoria '{columna}'")

        print("Validación de esquema completada.")

    def mostrar_resumen(self):
        print(self.datos.describe(include='all') if self.datos is not None else "No hay datos")
