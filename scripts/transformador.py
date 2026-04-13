#!/usr/bin/env python3
import pandas as pd
import os
from db import engine

def transformar_datos():
    archivo_entrada = 'data/clima.csv'
    archivo_salida = 'data/clima_transformado.csv'

    if not os.path.exists(archivo_entrada):
        print(f"❌ No existe {archivo_entrada}")
        return

    df = pd.read_csv(archivo_entrada)

    # 🔥 LIMPIEZA
    df = df.dropna()

    # 🔥 CONVERTIR NUMÉRICOS
    columnas_numericas = ['temperatura', 'sensacion_termica', 'humedad', 'velocidad_viento', 'codigo_tiempo']
    for col in columnas_numericas:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # 🔥 CLASIFICACIÓN
    def clasificar_temp(t):
        if t < 18:
            return 'Frío'
        elif t <= 28:
            return 'Templado'
        else:
            return 'Caluroso'

    df['clasificacion_temperatura'] = df['temperatura'].apply(clasificar_temp)

    # 🔥 GUARDAR CSV
    df.to_csv(archivo_salida, index=False)

    # 🔥 CONVERTIR FECHA
    df['fecha_extraccion'] = pd.to_datetime(df['fecha_extraccion'])

    # 🔥 GUARDAR EN POSTGRESQL
    df.to_sql('clima', engine, if_exists='append', index=False)

    print("✅ Transformación completada")
    print(f"📁 Archivo generado: {archivo_salida}")
    print("✅ Datos guardados en PostgreSQL")
    print(df.to_string(index=False))


if __name__ == "__main__":
    transformar_datos()