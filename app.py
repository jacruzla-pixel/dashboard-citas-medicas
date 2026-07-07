import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar dataset
df = pd.read_csv("salud_mental.csv")

st.title("Dashboard de Monitoreo de Salud Mental")
st.write("Análisis descriptivo y predictivo del estado de salud mental de estudiantes.")

# Mostrar registros
st.subheader("Vista previa del Dataset")
st.dataframe(df.head())

# -------------------------------
# Riesgo Psicosocial
# -------------------------------
st.subheader("Distribución del Riesgo Psicosocial")

riesgo = df["categoria_riesgo"].value_counts().reset_index()
riesgo.columns = ["Categoría", "Cantidad"]

fig1 = px.bar(
    riesgo,
    x="Categoría",
    y="Cantidad",
    title="Distribución del Riesgo Psicosocial"
)

st.plotly_chart(fig1)

# -------------------------------
# Estado del Seguimiento
# -------------------------------
st.subheader("Estado del Seguimiento Psicológico")

fig2 = px.pie(
    df,
    names="estado_seguimiento",
    title="Estado del Seguimiento"
)

st.plotly_chart(fig2)

# -------------------------------
# Evaluaciones por Mes
# -------------------------------
df["fecha"] = pd.to_datetime(df["fecha"])
df["mes"] = df["fecha"].dt.month

evaluaciones_mes = df.groupby("mes").size().reset_index(name="cantidad")

st.subheader("Evaluaciones por Mes")

fig3 = px.line(
    evaluaciones_mes,
    x="mes",
    y="cantidad",
    markers=True,
    title="Número de Evaluaciones por Mes"
)

st.plotly_chart(fig3)
