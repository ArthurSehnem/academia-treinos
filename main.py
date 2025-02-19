import streamlit as st
import pandas as pd
import os

excel_file = "treinos.xlsx"

if os.path.exists(excel_file):
    df = pd.read_excel(excel_file)
else:
    df = pd.DataFrame(columns=["Data", "Tipo", "Duração (min)", "Calorias"])

st.title("📋 Registro de Treinos")

with st.form("Registro"):
    data = st.date_input("📅 Data do treino")
    tipo = st.selectbox("🏋️ Tipo de treino", ["Cardiovascular", "Pernas", "Costas e Bíceps", "Peito, Tríceps e Ombros"])
    duracao = st.number_input("⏱️ Duração (min)", min_value=1, max_value=1000, step=1)
    calorias = st.number_input("🔥 Calorias", min_value=1, max_value=5000, step=1)
    submit = st.form_submit_button("Salvar")

if submit:
    novo_treino = pd.DataFrame([[data, tipo, duracao, calorias]], columns=["Data", "Tipo", "Duração (min)", "Calorias"])
    df = pd.concat([df, novo_treino], ignore_index=True)
    df.to_excel(excel_file, index=False)    
    st.success("✅ Treino registrado com sucesso!")
