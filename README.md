# 🐍 Mi Proyecto Flask con SQLite

¡Bienvenido! Este es un proyecto backend construido con **Python Flask**. Utiliza una base de datos **SQLite** ligera y está configurado para un desarrollo rápido y sencillo.

Este documento te guiará paso a paso para configurar tu entorno y lanzar la aplicación. 🚀

---

## 📋 Tabla de Contenidos
1. [Requisitos Previos](#-requisitos-previos)
2. [Instalación del Entorno](#-instalación-del-entorno)
3. [Configuración de la Base de Datos](#-configuración-de-la-base-de-datos)
4. [Ejecutar el Proyecto](#-ejecutar-el-proyecto)
5. [Estructura de Archivos](#-estructura-de-archivos)

---

## 🛠 Requisitos Previos

Antes de empezar, asegúrate de tener instalado en tu computadora:

* **Python 3.8+**: [Descargar aquí](https://www.python.org/downloads/)
* **Git** (Opcional, para clonar el repo).

---

## ⚙️ Instalación del Entorno

Sigue estos pasos para aislar las librerías del proyecto y evitar conflictos.

### 1. Clonar o descargar el proyecto
Abre tu terminal y ubícate en la carpeta del proyecto:
```bash
cd ruta/a/mi-proyecto-flask
2. Crear el Entorno Virtual (Virtualenv) 🛡️
Esto crea una carpeta "burbuja" para tus librerías.

En Windows:

Bash

python -m venv venv
En macOS / Linux:

Bash

python3 -m venv venv
3. Activar el Entorno 🔌
Debes activarlo cada vez que vayas a trabajar en el proyecto.

En Windows:

Bash

venv\Scripts\activate
En macOS / Linux:

Bash

source venv/bin/activate
Verás (venv) al inicio de tu terminal indicando que estás dentro.

4. Instalar Dependencias 📦
Instala Flask y otras herramientas necesarias listadas en el archivo requirements.txt:

Bash

pip install -r requirements.txt
🗄️ Configuración de la Base de Datos
Este proyecto usa SQLite (una base de datos en un solo archivo).

Asegúrate de tener el código de conexión en tu archivo principal (ej. app.py).

Si el proyecto incluye un script de inicialización (como init_db.py o similar), ejecútalo ahora:

Bash

# Ejemplo (si aplica en tu proyecto):
python init_db.py
(Si no hay script, la base de datos database.db se creará automáticamente al ejecutar la app por primera vez si así está programado).

▶️ Ejecutar el Proyecto
Para lanzar el servidor de desarrollo indicando el archivo específico y con el modo Debug activado (para ver errores en tiempo real y recarga automática), usa el siguiente comando.

Supongamos que tu archivo principal se llama app.py (cámbialo si se llama diferente):

Bash

flask --app app.py --debug run
Una vez ejecutado, verás algo como esto:

Running on https://www.google.com/search?q=http://127.0.0.1:5000

👉 Abre esa dirección en tu navegador para ver tu web.

📂 Estructura de Archivos
Para que no te pierdas, así está organizado el proyecto:

Plaintext

mi-proyecto/
│
├── venv/                # 🚫 Entorno virtual (NO tocar)
├── app.py               # 🧠 Archivo principal de la aplicación
├── requirements.txt     # 📄 Lista de librerías a instalar
├── database.db          # 🗄️ Archivo de base de datos SQLite
├── templates/           # 🎨 Archivos HTML
│   └── index.html
├── static/              # 🖼️ Imágenes, CSS y JavaScript
└── README.md            # 📖 Estas instrucciones

🆘 Solución de Problemas Comunes
Error: "flask no se reconoce como un comando": Asegúrate de haber activado el entorno virtual (venv) antes de ejecutar el comando.

Error de conexión a la base de datos: Verifica que el archivo .db tenga permisos de escritura o que la ruta sea correcta.

¡Disfruta programando! Hecho con ❤️ y Python.

---

### Lo que necesitas para que este README funcione al 100%:

1.  **El archivo `requirements.txt`**: Crea un archivo con ese nombre y pon dentro al menos esto:
    ```text
    Flask
    ```
    *(Nota: `sqlite3` no se pone aquí porque ya viene instalado dentro de Python por defecto).*

2.  **El nombre del archivo**: En la sección "Ejecutar el proyecto", he puesto `app.py`. Si tu archivo se llama diferente (ej. `main.py`), edita esa línea en el README antes de subirlo.
