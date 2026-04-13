import schedule
import time
import subprocess

def ejecutar_etl():
    print("Ejecutando ETL automáticamente...")

    subprocess.run(["python3", "scripts/etl.py"])

# Ejecutar cada 1 hora
schedule.every(1).hours.do(ejecutar_etl)

print("Scheduler iniciado...")

while True:
    schedule.run_pending()
    time.sleep(60)
