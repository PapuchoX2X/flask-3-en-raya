
# 3 en Raya - Flask Web App 🎮

Este es un proyecto desarrollado en **Python** utilizando el framework **Flask**. El objetivo es practicar la lógica de programación, el manejo de estados mediante sesiones y la implementación de contenedores con **Docker**.

## 📁 Estructura del Proyecto
```text
.
├── app.py              # Lógica del servidor y el juego
├── Dockerfile          # Instrucciones de contenedorización
├── requirements.txt    # Dependencias del proyecto
├── .gitignore          # Archivos excluidos de Git
└── templates/          # Vistas HTML
    └── index.html      # Interfaz de usuario del juego
```

## 🚀 Ejecución Local (Flask + Entorno Virtual)

Sigue estos pasos para ejecutar la aplicación directamente en tu sistema operativo (Windows o Linux).

### 1. Configuración del Entorno

#### Clonar el repositorio:

```bash
git clone https://github.com/PapuchoX2X/flask-3-en-raya.git
cd flask-3-en-raya
```

#### Crear y activar el entorno virtual:

**En Windows:**

```powershell
python -m venv venv
.
env\Scripts\Activate.ps1
```

**En Linux (Debian/Ubuntu):**

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Instalar dependencias:

```bash
pip install -r requirements.txt
```

#### Ejecutar la aplicación:

```bash
python app.py
```

Accede desde tu navegador a: [http://localhost:5000](http://localhost:5000)

## 🐳 Ejecución con Docker (Contenedorización)

Ideal para despliegues en servidores o máquinas virtuales sin necesidad de configurar Python manualmente.

### 1. Construcción y Despliegue

#### Construir la imagen de Docker:

```bash
docker build -t 3-en-raya .
```

#### Correr el contenedor:

```bash
docker run -d -p 5000:5000 --name tictactoe 3-en-raya
```

### 2. Acceso

- Si estás en la misma máquina: [http://localhost:5000](http://localhost:5000)
- Si accedes a una VM desde el host: [http://<IP_DE_TU_VM>:5000](http://<IP_DE_TU_VM>:5000)

## 💻 Dependencias

- **Flask**: Para la creación del servidor web.
- **Docker**: Para la contenedorización del proyecto.

## 👨‍💻 Desarrollado por

**PapuchoX2X**  
Ingeniería en Telecomunicaciones
