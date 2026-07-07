import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar el dataset
df = pd.read_csv('salud_mental.csv')

st.title('Dashboard de Monitoreo de Salud Mental')

st.subheader('Estudiantes por Nivel de Riesgo')
fig1 = px.bar(
    df['categoria_riesgo'].value_counts(),
    labels={'value': 'Cantidad', 'index': 'Nivel de Riesgo'}
)
st.plotly_chart(fig1)

st.subheader('Estado del Seguimiento Psicológico')
fig2 = px.pie(
    df,
    names='estado_seguimiento'
)
st.plotly_chart(fig2)

df['fecha'] = pd.to_datetime(df['fecha'])
df['mes'] = df['fecha'].dt.month
evaluaciones_mes = df.groupby('mes').size().reset_index(name='cantidad')

st.subheader('Evaluaciones por Mes')
fig3 = px.line(
    evaluaciones_mes,
    x='mes',
    y='cantidad',
    markers=True
)
st.plotly_chart(fig3)
df = pd.read_csv('salud_mental.csv')
