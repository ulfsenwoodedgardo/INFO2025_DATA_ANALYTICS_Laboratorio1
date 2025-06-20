# INFO2025 - Análisis de Datos - Laboratorio 1

## Descripción

Aplicación modular en Python que permite cargar automáticamente diferentes tipos de archivos de datos (`.csv`, `.xlsx`, `.json`, `.txt`), realizar validaciones básicas, transformaciones y guardar los datos en una base de datos relacional MySQL mediante SQLAlchemy.

Este proyecto cumple con los cuatro pilares de la Programación Orientada a Objetos (POO):  
    **Abstracción, Encapsulamiento, Herencia, Polimorfismo**.

## Estructura de la aplicación

- `main.py`: script principal de ejecución.
- `app_loader.py`: clase que organiza la carga de archivos y persistencia.
- `domain/`: clases relacionadas a los datasets y POO.
- `data/`: clase para la persistencia con SQLAlchemy.
- `files/`: carpeta que contiene los archivos de datos a procesar.
- `.env`: configuración de acceso a la base de datos (NO se sube a GitHub).

## Requisitos

- Python 3.10 o superior
- MySQL Server 8.x
- Librerías del archivo `requirements.txt`

## Instalación

1. Clonar el repositorio:
    ```

    git clone https://github.com/ulfsenwoodedgardo/INFO2025_DATA_ANALYTICS_Laboratorio1.git

    cd INFO2025_ANALISIS_DATOS_LAB1

    ```

2. Crear un entorno virtual:

    ```
    python -m venv venv
    ```

3. Activar el entorno virtual:

    * En Windows:

        ```
        venv\Scripts\activate
        ```

    * En Linux/Mac:

        ```
        source venv/bin/activate
        ```

4. Instalar dependencias:

    ```
    pip install -r requirements.txt
    ```
    
5. Configurar `.env` con las credenciales de tu base de datos.

## Ejecución

Ejecutar desde la terminal:

    python main.py

    El sistema cargará automáticamente los archivos del directorio `/files/`, realizará las validaciones y guardará cada dataset en una tabla de la base de datos MySQL.

## Autor

Nombre del autor: **Edgardo Nicolás**
Curso: **INFO2025 - Análisis de Datos**

