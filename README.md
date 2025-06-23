
# INFO2025 - Análisis de Datos - Laboratorio 1

### Descripción

Aplicación modular en Python que permite:

- Cargar múltiples formatos de datos: `.csv`, `.xlsx`, `.json`, `.txt`, APIs REST
- Validar y transformar los datos
- Guardar los datos en una base de datos relacional mediante SQLAlchemy
- Ejecutarse desde la consola mediante una clase principal

Proyecto desarrollado para la certificación **INFO2025 - Data Analytics**.

---

### Requisitos del sistema

- Python 3.10 o superior
- MySQL (u otro motor de base compatible con SQLAlchemy)

---

### Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/ulfsenwoodedgardo/INFO2025_DATA_ANALYTICS_Laboratorio1.git

cd INFO2025_DATA_ANALYTICS_Laboratorio1
````

2. Crear y activar un entorno virtual:

```bash
# Windows
python -m venv venv
venv\Scripts\activate.bat

# Linux / Mac
python3 -m venv venv
source venv/bin/activate
```

3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

4. Configurar las variables de entorno:

* Renombrar el archivo `.env.example` a `.env`
* Completar los datos de conexión a la base de datos:

```env
DB_USER=tu_usuario_mysql
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_NAME=tu_base_datos
DB_PORT=3306
```

---

### Configuración de APIs

Las APIs que se procesan están definidas en el archivo `app_loader.py`, en la variable:

```python
self.api_urls = [
    ("URL_API", "key_path"),
    ...
]
```

**Ejemplo:**

```python
self.api_urls = [
    ("https://apis.datos.gob.ar/georef/api/provincias", "provincias")
]
```

El parámetro `"key_path"` indica qué clave del JSON contiene la lista principal de datos a cargar en tabla.

---

### Ejecución

Desde la raíz del proyecto, ejecutar:

```bash
python main.py
```

El sistema realiza:

1. Carga automática de todos los archivos en `/files/`
2. Procesamiento de APIs configuradas
3. Validación y transformación de datos
4. Guardado en la base de datos en tablas separadas
5. Reporte de resultados en consola

---

### Tecnologías utilizadas

* Python 3.10+
* Pandas
* SQLAlchemy
* PyMySQL
* python-decouple
* python-dotenv
* requests

---

### Autor

**Edgardo Nicolás**
INFO2025 - Data Analytics 2025

---

### Licencia

Este proyecto es de uso educativo, sin licencia comercial.
