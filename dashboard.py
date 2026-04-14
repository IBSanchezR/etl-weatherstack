import os
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

st.set_page_config(page_title="Dashboard Clima", layout="wide")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://clima_user:Admin123@postgres:5432/clima_db"
)

engine = create_engine(DATABASE_URL)

@st.cache_data(ttl=60)
def cargar_datos():
    query = "SELECT * FROM clima ORDER BY fecha_extraccion DESC"
    return pd.read_sql(query, engine)

st.title("🌍 Dashboard Climático")

try:
    df = cargar_datos()

    if df.empty:
        st.warning("No hay datos en la tabla clima.")
    else:
        df["fecha_extraccion"] = pd.to_datetime(df["fecha_extraccion"])

        st.subheader("Datos")
        st.dataframe(df, use_container_width=True)

        st.subheader("Temperatura por ciudad")
        fig = px.bar(df, x="ciudad", y="temperatura", color="ciudad")
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Humedad por ciudad")
        fig2 = px.bar(df, x="ciudad", y="humedad", color="ciudad")
        st.plotly_chart(fig2, use_container_width=True)

except Exception as e:
    st.error(f"Error al conectar o consultar la base de datos: {e}")