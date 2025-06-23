Te paso tu README **ajustado**, solo reordenando la parte de las APIs (sin cambiar nada más), listo para que lo pegues:

---

````markdown
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
- Entorno virtual recomendado (venv)

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

### Ejecución

Desde la raíz del proyecto, ejecutar:

```bash
python main.py
```

El sistema realiza:

1. Carga todos los archivos de `/files/` (.csv, .xlsx, .json, .txt)
2. Aplica validaciones y transformaciones automáticas
3. Guarda los datos en la base en tablas separadas por archivo
4. Informa resultados en consola

---

### Soporte para APIs REST

* Procesa las APIs definidas en `AppLoader`
* Soporte de `key_path` configurable para extraer arrays de datos desde JSON anidados
* Los resultados son almacenados en la base de datos como tablas equivalentes a las APIs

---

### Principios de POO aplicados

* **Abstracción**: separación clara entre lectura, validación y persistencia
* **Encapsulamiento**: atributos y métodos privados donde corresponde
* **Herencia**: clases derivadas a partir de una clase base `Dataset`
* **Polimorfismo**: métodos redefinidos para manejar distintos formatos de archivo/API

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
