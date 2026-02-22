# ETL Weatherstack (WSL + Python)

Pipeline ETL para extraer datos de clima desde Weatherstack, transformarlos y guardarlos en CSV/JSON, además de generar gráficas.

## Requisitos
- Python 3.11+
- WSL Ubuntu
- API Key de Weatherstack
- Git

## Instalación

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## Ejecutar

python scripts/extractor.py
python scripts/visualizador.py
