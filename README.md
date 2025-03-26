# 🧠 Facial Access Control - Setup Guide

Este documento describe los pasos necesarios para preparar una máquina desde cero y ejecutar correctamente el proyecto `facial-access-control`.

---

## ✅ Requisitos del sistema

- **Sistema operativo**: Linux (probado en Ubuntu/Debian)
- **Python**: Versión 3.10
- **Acceso a terminal con privilegios sudo**
- **Cámara web funcional**

---

## 📦 Dependencias del sistema

Primero instala los paquetes necesarios para compilar Python y usar interfaces gráficas (Tkinter):

```bash
sudo apt update
sudo apt install -y make build-essential libssl-dev zlib1g-dev \
  libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
  libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev \
  python3-pip python3-tk cmake
```

> Si no tienes Python 3.10 instalado, puedes instalarlo manualmente desde el código fuente.

---

## 🐍 Instalación de Python 3.10 (si no está disponible en tu sistema)

```bash
cd /tmp
wget https://www.python.org/ftp/python/3.10.13/Python-3.10.13.tgz
tar -xf Python-3.10.13.tgz
cd Python-3.10.13
./configure --enable-optimizations
make -j$(nproc)
sudo make altinstall
```

Verifica que se haya instalado:

```bash
python3.10 --version
```

---

## 🌱 Crear y activar entorno virtual

Desde la raíz del proyecto:

```bash
python3.10 -m venv venv
source venv/bin/activate
```

---

## 📦 Instalar dependencias de Python

Con el entorno virtual activado, instala:

```bash
pip install --upgrade pip
pip install opencv-python mediapipe numpy pandas imutils tensorboard pydantic
```

---

## 🚀 Ejecutar el proyecto

Dentro del entorno virtual, ejecuta:

```bash
python examples/example.py
```

Esto debería lanzar la interfaz gráfica del sistema de control de acceso facial.

---

## 📌 Notas

- `mediapipe` no es compatible con Python 3.12 al momento de escribir esta guía. Usa **Python 3.10**.
- El sistema requiere **cámara web activa**.
- Este proyecto depende de bibliotecas como `tkinter`, `pydantic`, y `tensorboard` para la interfaz y el procesamiento de imágenes.
