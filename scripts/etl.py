from extractor import main as extraer_clima
from transformador import transformar_datos
import subprocess

def run_etl():
    print("Iniciando proceso ETL...")

    # 🔥 EXTRACCIÓN
    extraer_clima()

    # 🔥 TRANSFORMACIÓN + DB
    transformar_datos()

    # 🔥 VISUALIZACIÓN
    subprocess.run(["python3", "scripts/visualizador.py"])

    print("ETL completado")


if __name__ == "__main__":
    run_etl()