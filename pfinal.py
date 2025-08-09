import streamlit as st
import mysql.connector
import os

try:
    conn = mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        port=int(os.environ.get("DB_PORT")),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_DATABASE")
    )
    cursor = conn.cursor()
    st.success("Conexión a la base de datos establecida correctamente. ✅")
except Exception as e:
    st.error(f"Error al conectar con la base de datos: {e}. Por favor, verifica tus variables de entorno.")
    st.stop()

st.title("UNIVERSIDAD TECNOLOGICA SANTA CATARINA")
st.subheader("Jorge Eduardo Pérez Juárez")
st.subheader("Matricula: 24155")
st.title("Registro de estudiantes")

apellidos = st.text_input("Apellidos")
nombres = st.text_input("Nombres")
matricula = st.number_input("Matrícula", min_value=0, step=1, format="%d")
correo = st.text_input("Correo")

if st.button("Guardar en base de datos"):
    if apellidos and nombres and matricula is not None and correo:
        try:
            sql = "INSERT INTO registros (apellidos, nombres, matricula, correo) VALUES (%s, %s, %s, %s)"
            valores = (apellidos, nombres, matricula, correo)
            cursor.execute(sql, valores)
            conn.commit()
            st.success("Registro guardado con éxito. 🎉")
        except mysql.connector.Error as err:
            st.error(f"Error al guardar el registro: {err}")
    else:
        st.warning("Por favor, complete todos los campos antes de guardar. ⚠️")

st.subheader("Registros guardados")
try:
    cursor.execute("SELECT id, apellidos, nombres, matricula, correo FROM registros")
    registros = cursor.fetchall()

    if registros:
        for fila in registros:
            st.write(f"**ID:** {fila[0]} | **Apellidos:** {fila[1]} | **Nombres:** {fila[2]} | **Matrícula:** {fila[3]} | **Correo:** {fila[4]}")
    else:
        st.info("No hay registros guardados aún.")
except mysql.connector.Error as err:
    st.error(f"Error al cargar los registros: {err}")