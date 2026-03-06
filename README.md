# ETL Weatherstack - Extracción de Datos de Clima

Proyecto de Minería de Datos que implementa un pipeline ETL completo para extraer, transformar y visualizar datos de clima usando la Weatherstack API.

Repositorio:
https://github.com/IBSanchezR/etl-weatherstack

---

## 🎯 Objetivo

Aprender las fases principales de un proceso ETL profesional:

1. Extract – Obtener datos de APIs externas  
2. Transform – Procesar y limpiar los datos  
3. Load – Guardar la información en diferentes formatos  
4. Visualize – Analizar y representar los datos

---

## 🚀 Quick Start

### Requisitos

- Python 3.11+
- pip
- Git
- WSL Ubuntu (opcional)

---

## Instalación

Clonar el repositorio:

git clone https://github.com/IBSanchezR/etl-weatherstack.git  
cd etl-weatherstack  

Crear entorno virtual:

python3 -m venv venv  
source venv/bin/activate  

En Windows:

venv\Scripts\activate  

Instalar dependencias:

pip install -r requirements.txt  

Configurar la API Key:

echo "API_KEY=tu_api_key_aqui" > .env

---

## Ejecutar el Pipeline ETL

Ejecutar extracción de datos:

python scripts/extractor.py  

Transformar datos:

python scripts/transformador.py  

Generar visualizaciones:

python scripts/visualizador.py  

---

## 📊 Salida del Pipeline

El proyecto genera automáticamente:

- data/clima.csv → Datos en formato CSV  
- data/clima_raw.json → Datos originales en JSON  
- data/clima_transformado.csv → Datos procesados  
- data/clima_analysis.png → Gráfica de análisis  
- logs/etl.log → Registro de ejecución  

---

## 📁 Estructura del Proyecto

etl-weatherstack/

scripts/  
 ├ extractor.py  
 ├ transformador.py  
 └ visualizador.py  

data/  
 ├ clima.csv  
 ├ clima_raw.json  
 ├ clima_transformado.csv  
 └ clima_analysis.png  

logs/  
 └ etl.log  

.env  
.gitignore  
requirements.txt  
README.md  

---

## 🔑 Obtener API Key

1. Ir a https://weatherstack.com  
2. Crear una cuenta gratuita  
3. Copiar la Access Key  
4. Guardarla en el archivo `.env`

API_KEY=tu_api_key

---

## 📚 Conceptos Aplicados

Este proyecto aplica conceptos de:

- ETL Pipeline
- Consumo de APIs REST
- Python para ingeniería de datos
- Manejo de logs
- Variables de entorno
- Visualización de datos
- Versionamiento con Git y GitHub

---

## 🛠️ Tecnologías

- Python 3.11
- requests
- pandas
- matplotlib
- python-dotenv
- Git
- GitHub

---

## 👨‍💻 Autor

Brandon Sanchez  
Ingeniería de Sistemas  
CORHUILA

---

## Estado del Proyecto

Pipeline ETL funcional

✔ Extracción  
✔ Transformación  
✔ Visualización  
✔ Versionado con Git  
✔ Publicado en GitHub