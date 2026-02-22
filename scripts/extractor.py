import os
import json
import logging
import time
from datetime import datetime

import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

os.makedirs("data", exist_ok=True)
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/etl.log"),
        logging.StreamHandler()
    ],
)

logger = logging.getLogger(__name__)

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("WEATHERSTACK_BASE_URL", "https://api.weatherstack.com").rstrip("/")
CIUDADES = [c.strip() for c in os.getenv("CIUDADES", "Bogota,Neiva").split(",") if c.strip()]


def extraer(ciudad: str) -> dict:
    url = f"{BASE_URL}/current"
    params = {
        "access_key": API_KEY,
        "query": ciudad
    }

    response = requests.get(url, params=params, timeout=15)

    if response.status_code != 200:
        raise ValueError(f"HTTP {response.status_code} en {ciudad}")

    return response.json()


def transformar(raw: dict) -> dict:
    if raw.get("error"):
        raise ValueError(raw["error"].get("info", "Error en API"))

    loc = raw.get("location", {})
    cur = raw.get("current", {})

    return {
        "ciudad": loc.get("name"),
        "pais": loc.get("country"),
        "latitud": loc.get("lat"),
        "longitud": loc.get("lon"),
        "temperatura": cur.get("temperature"),
        "sensacion_termica": cur.get("feelslike"),
        "humedad": cur.get("humidity"),
        "velocidad_viento": cur.get("wind_speed"),
        "descripcion": (cur.get("weather_descriptions") or ["N/A"])[0],
        "fecha_extraccion": datetime.now().isoformat(timespec="seconds"),
        "codigo_tiempo": cur.get("weather_code"),
    }


def main():
    if not API_KEY:
        raise ValueError("API_KEY no configurada en .env")

    filas = []

    for ciudad in CIUDADES:
        try:
            raw = extraer(ciudad)
            fila = transformar(raw)
            filas.append(fila)
            logger.info(f"OK: {ciudad}")
        except Exception as e:
            logger.error(f"Error en {ciudad}: {e}")

        time.sleep(2)

    with open("data/clima_raw.json", "w", encoding="utf-8") as f:
        json.dump(filas, f, ensure_ascii=False, indent=2)

    df = pd.DataFrame(filas)
    df.to_csv("data/clima.csv", index=False, encoding="utf-8")

    if not df.empty:
        print(df.to_string(index=False))
    else:
        print("No se extrajeron datos.")


if __name__ == "__main__":
    main()
