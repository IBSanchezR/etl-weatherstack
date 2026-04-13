import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

st.set_page_config(page_title="Dashboard Clima", layout="wide")

# conexión
engine = create_engine(
    "postgresql+psycopg2://clima_user:Admin123@localhost:5432/clima_db"
)

@st.cache_data(ttl=60)
def cargar_datos():
    return pd.read_sql("SELECT * FROM clima ORDER BY fecha_extraccion DESC", engine)

st.title("🌍 Dashboard Climático")

df = cargar_datos()

if df.empty:
    st.warning("No hay datos")
else:
    df["fecha_extraccion"] = pd.to_datetime(df["fecha_extraccion"])

    st.subheader("Datos")
    st.dataframe(df)

    st.subheader("Temperatura por ciudad")
    fig = px.bar(df, x="ciudad", y="temperatura", color="ciudad")
    st.plotly_chart(fig)

    st.subheader("Humedad por ciudad")
    fig2 = px.bar(df, x="ciudad", y="humedad", color="ciudad")
    st.plotly_chart(fig2)
