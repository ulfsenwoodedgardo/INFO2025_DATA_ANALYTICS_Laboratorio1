````markdown
# INFO2025 - Análisis de Datos - Laboratorio 1

### Descripción

Aplicación modular en Python que permite:

- Cargar múltiples formatos de datos (.csv, .xlsx, .json, .txt, APIs REST)
- Validar datos básicos
- Guardar los datos en una base de datos relacional utilizando SQLAlchemy
- Ejecutarse fácilmente desde la consola mediante una clase principal

Proyecto desarrollado para la certificación **INFO2025 - Data Analytics**.

---

### Requisitos del sistema

- Python 3.10 o superior
- MySQL Server (instalado y corriendo)

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
* Completar los datos de conexión a la base de datos en `.env`

```env
DB_USER=tu_usuario_mysql
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_NAME=tu_base_datos
DB_PORT=tu_puerto
```

---

### Ejecución

Desde la raíz del proyecto, ejecutar:

```bash
python main.py
```

El sistema:

1. Carga todos los archivos del directorio `/files/`
2. Procesa las APIs definidas en `app_loader.py`
3. Aplica validaciones y transformaciones
4. Guarda los datos en la base en tablas separadas por archivo/API
5. Informa resultados en consola

---

### Tecnologías usadas

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
© INFO2025 - Data Analytics 2025
