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

```bash
git clone https://github.com/ulfsenwoodedgardo/INFO2025_DATA_ANALYTICS_Laboratorio1.git
cd INFO2025_ANALISIS_DATOS_LAB1
