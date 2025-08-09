import streamlit as st
import mysql.connector

conn = mysql.connector.connect(
    host="gondola.proxy.rlwy.net", 
    port=38111,  
    user="root",
    password="XbZIsALMFmhSmTAfkDGftdgzcTsCjQMx",
    database="awos"
)
cursor = conn.cursor()

st.title("UNIVERSIDAD TECNOLOGICA SANTA CATARINA")
st.subheader("Jorge Eduardo Pérez Juárez")
st.subheader("Matricula: 24155")
st.title("Registro de estudiantes")

apellidos = st.text_input("Apellidos")
nombres = st.text_input("Nombres")
matricula = st.number_input("Matrícula", min_value=0, step=1)
correo = st.text_input("Correo")

if st.button("Guardar en base de datos"):
    if apellidos and nombres and matricula and correo:
        sql = "INSERT INTO registros (apellidos, nombres, matricula, correo) VALUES (%s, %s, %s, %s)"
        valores = (apellidos, nombres, matricula, correo)
        cursor.execute(sql, valores)
        conn.commit()
        st.success("Registro guardado con éxito.")
    else:
        st.warning("Por favor, complete todos los campos.")

st.subheader("Registros guardados")
cursor.execute("SELECT * FROM registros")
for fila in cursor.fetchall():
    st.write(f"{fila[0]} | {fila[1]} | {fila[2]} | {fila[3]} | {fila[4]}")
