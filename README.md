# 🚀 Flask Project Starter

Este es un proyecto base para iniciar una aplicación web con **Python Flask** y base de datos **SQLite**. Está configurado para ser fácil de instalar y ejecutar.

---

## 📋 Requisitos Previos

* **Python 3.8** o superior.
* **Git** (opcional).

---

## ⚙️ Instalación Paso a Paso

### 1. Preparar el Entorno Virtual
Es necesario crear un entorno virtual para aislar las librerías del proyecto.

**En Windows:**

python -m venv venv 
venv\Scripts\activate

**En macOS / Linux:**

python3 -m venv venv 
source venv/bin/activate


Nota: Sabrás que el entorno está activo porque verás (venv) al principio de tu terminal.

### 2. Instalar Dependencias
Una vez activado el entorno, instala las librerías necesarias (Flask, etc.):

pip install -r requirements.txt


### 🗄️ Base de Datos (SQLite)

Este proyecto utiliza SQLite.

No necesitas instalar ningún servidor de base de datos extra.

El archivo de la base de datos (normalmente .db o .sqlite) se generará automáticamente en esta carpeta o ya estará incluido.

La librería sqlite3 viene incluida por defecto en Python.

### ▶️ Cómo Ejecutar el Proyecto

Para lanzar el servidor en modo desarrollo (con recarga automática y depuración de errores), usa el siguiente comando en tu terminal:

python manage.py

Nota: Si no ejecutamos el anterior comando, no funcionara porque no se habrá creado la BD correctamente.

flask --app app.py --debug run

--app app.py: Indica que el archivo principal es app.py.

--debug: Activa el modo debug (reinicia el servidor al guardar cambios).

run: Inicia el servidor.

Una vez ejecutado, abre tu navegador en: 👉 http://127.0.0.1:5000

---

## 🆘 Solución de Problemas

Error: "flask" no se reconoce como un comando interno o externo.

Solución: Asegúrate de haber activado el entorno virtual (venv) antes de ejecutar el comando.

Error: ModuleNotFoundError

Solución: Ejecuta pip install -r requirements.txt de nuevo con el entorno activado.
