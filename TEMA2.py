import streamlit as st
import pandas as pd
import plotly.express as px


data = pd.read_csv('https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv')
data1=data
data2=data
data3=data

st.title("TEMA 3: Gráficas en Streamlit")
st.subheader("Luis Camilo Angel Sesma")
st.subheader("A01253231")
st.subheader("Descripción breve:")
st.write("Desarrollar un código sobre la estructura de una aplicación web que contenga 3 controles (radio, selectbox y slider) sobre el proyecto de visualización de analítica de datos para WalMart USA. ")

st.subheader("Gráfica: Histograma")

selección_state=data1["Segment"].unique().tolist()
state=st.selectbox("¿Qué segmento quieres ver?", selección_state, 0)
db1=data1[data1["Segment"]==state]

fig5 = px.histogram(db1,x='State')

st.plotly_chart(fig5, use_container_width=True)


st.subheader("Gráfica: Pastel")

fig1 = px.pie(data2, values='Sales', names='Ship Mode', color_discrete_sequence=px.colors.sequential.RdBu)

st.plotly_chart(fig1, use_container_width=True)


st.subheader("Gráfica: Barras")

opc_region=st.radio("Clase", key="visibility", options=["South","West","Central","East"])
region=data3[data3["Region"]==opc_region]

fig3 = px.bar(region, x='City', y='Sales', color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig3, use_container_width=True)