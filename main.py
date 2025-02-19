import streamlit as st
import mysql.connector

# Função para conectar ao MySQL
def conectar_bd():
    return mysql.connector.connect(
        host="localhost",      # Altere se necessário
        user="root",    # Substitua pelo seu usuário do MySQL
        password="",  # Substitua pela senha
        database="academia"    # Nome do banco de dados
    )

st.title("📋 Registro de Treinos")

# Formulário para entrada de dados
with st.form("Registro"): 
    data = st.date_input("📅 Data do treino")
    tipo = st.selectbox("🏋️ Tipo de treino", ["Cardiovascular", "Pernas", "Costas e Bíceps", "Peito, Tríceps e Ombros"])
    duracao = st.number_input("⏱️ Duração (min)", min_value=1, max_value=1000, step=1)
    calorias = st.number_input("🔥 Calorias", min_value=1, max_value=5000, step=1)
    submit = st.form_submit_button("Salvar")

if submit:
    conexao = None
    cursor = None

    try:
        conexao = conectar_bd()
        cursor = conexao.cursor()

        sql = "INSERT INTO treinos (data, tipo, duracao, calorias) VALUES (%s, %s, %s, %s)"
        valores = (data, tipo, duracao, calorias)

        cursor.execute(sql, valores)
        conexao.commit()

        st.success("✅ Treino registrado com sucesso!")

    except Exception as e:
        st.error(f"❌ Erro ao salvar o treino: {e}")

    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
