# OPTIMUS: Automatización de Mantenimientos para el Laboratorio de Microsoft

## Análisis de la Situación Actual

En el Laboratorio de Microsoft de la Facultad de Ciencias e Ingeniería, el proceso de control de mantenimientos se maneja de manera manual, lo que lleva a una gestión ineficiente de los recursos y puede causar interrupciones en las actividades educativas. El Ing. Alian Chavarria coordina las actividades y servicios, enfrentando desafíos debido al método actual de revisión y reparación de equipos.

## Impacto del Proyecto

El proyecto OPTIMUS busca introducir una solución automatizada para la gestión de mantenimientos, mejorando significativamente la eficiencia operativa del laboratorio. Con la implementación de este sistema, esperamos:

- Reducir el tiempo de inactividad de los equipos mediante mantenimientos preventivos y correctivos más eficientes.
- Disminuir los costos asociados a reparaciones imprevistas.
- Mejorar la disponibilidad de equipos para actividades educativas.
- Facilitar la toma de decisiones con la generación de informes y alertas basadas en datos concretos.

## Estructura del Proyecto

El proyecto se organiza en una estructura modular, enfocada en la claridad y la mantenibilidad del código:

- `app/`: Contiene la lógica principal de la aplicación.
  - `data_processing/`: Módulos para procesar los datos extraídos de la base de datos y prepararlos para su uso o exportación.
  - `database/`: Scripts de conexión y operaciones relacionadas con la base de datos MySQL.
  - `drive_integration/`: Integración con la API de Google Drive para almacenar informes y logs.
  - `main.py`: Punto de entrada del programa que orquesta las operaciones de alto nivel.

## Comenzando

Para ejecutar el proyecto, asegúrate de tener Python 3.x instalado y sigue los siguientes pasos:

1. Instala las dependencias necesarias utilizando `pip`:

    ```bash
    pip install -r requirements.txt
    ```

2. Configura tus variables de entorno copiando el archivo `.env.example` a `.env` y ajustando los valores según tu entorno.

3. Ejecuta el script principal:

    Para iniciar el programa, simplemente ejecuta el archivo `main.py` utilizando Python. Esto iniciará el proceso de conexión a la base de datos, realizará las consultas necesarias, procesará los datos y opcionalmente, subirá los resultados a Google Drive o generará archivos CSV locales, según la configuración.

    ```bash
    python main.py
    ```

    Asegúrate de estar en el directorio raíz del proyecto antes de ejecutar este comando.
