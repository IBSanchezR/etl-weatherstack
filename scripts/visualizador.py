import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("data", exist_ok=True)

df = pd.read_csv("data/clima.csv")

# 1) Temperatura
plt.figure(figsize=(10,5))
plt.bar(df["ciudad"], df["temperatura"])
plt.title("Temperatura actual por ciudad (°C)")
plt.ylabel("°C")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("data/temperatura.png", dpi=200)
plt.close()

# 2) Humedad
plt.figure(figsize=(10,5))
plt.bar(df["ciudad"], df["humedad"])
plt.title("Humedad por ciudad (%)")
plt.ylabel("%")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("data/humedad.png", dpi=200)
plt.close()

# 3) Velocidad del viento
plt.figure(figsize=(10,5))
plt.bar(df["ciudad"], df["velocidad_viento"])
plt.title("Velocidad del viento por ciudad (km/h)")
plt.ylabel("km/h")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("data/viento.png", dpi=200)
plt.close()

print("✅ Gráficas generadas en la carpeta data/:")
print("- data/temperatura.png")
print("- data/humedad.png")
print("- data/viento.png")
