import streamlit as st
import pandas as pd
import requests # Para hablar con internet

# Configuración básica de la página
st.set_page_config(page_title="Rick & Morty Explorer", page_icon="🛸", layout="wide")

st.title("🛸 Explorador del Multiverso")
st.markdown("Esta app descarga datos reales de la API de Rick & Morty.")
st.header("1. Conexión a la API")

# URL de la API (La dirección de internet donde están los datos)
url = 'https://rickandmortyapi.com/api/character'

if st.button("📡 Descargar Datos"):
    with st.spinner('Contactando con el servidor...'):
        # 1. Hacemos la petición a la web
        respuesta = requests.get(url)
        
        # 2. Convertimos el texto recibido en un diccionario de Python (objetos) (JSON)
        datos_json = respuesta.json()
        # --- Con esto vemos los datos descargados ---
        st.write("👀 Así se ven los datos crudos (JSON):")
        st.json(datos_json) 
        # -----------------------------
        
        # 3. Extraemos la lista de personajes (están bajo la clave 'results'). Es un array (una lista en Python)
        lista_personajes = datos_json['results']
        
        # 4. MAGIA PANDAS: Convertimos la lista en una Tabla (DataFrame)
        df = pd.DataFrame(lista_personajes)
        
        # 5. Guardamos la tabla en la memoria de la App (Session State)
        # Esto sirve para no perder los datos cada vez que tocamos un botón
        st.session_state['mi_tabla'] = df
        
        st.success(f"¡Éxito! Se han descargado {len(df)} personajes.")
# Verificamos si la tabla existe en memoria
if 'mi_tabla' in st.session_state:
    df = st.session_state['mi_tabla']
    
    st.write("---")
    st.header("2. Analizando los Datos")

    # --- ZONA DE FILTROS ---
    col_filtro1, col_filtro2 = st.columns(2)
    
    with col_filtro1:
        # Filtro por Estado (Vivo, Muerto, Desconocido)
        estado = st.radio("Filtrar por estado:", ["Alive", "Dead", "unknown"], horizontal=True)
    
    # --- LÓGICA PANDAS ---
    # Traducido: "Del DataFrame (df), quédate con las filas donde la columna 'status' sea igual a lo que eligió el usuario"
    df_filtrado = df[df['status'] == estado]
    
    with col_filtro2:
        st.metric("Personajes encontrados", len(df_filtrado))

    # Mostramos la tabla interactiva (Solo columnas interesantes)
    st.dataframe(df_filtrado[['status','name', 'species','gender']])

    # --- GALERÍA DE IMÁGENES ---
    st.header(f"Galería de personajes ({estado})")
    
    # Mostramos los primeros 3 personajes encontrados para no saturar
    cols = st.columns(3)
    
    # Recorremos solo los 3 primeros del filtro
    for i in range(min(3, len(df_filtrado))):
        personaje = df_filtrado.iloc[i] # Cogemos la fila del personaje
        with cols[i]:
            st.image(personaje['image'], caption=personaje['name'], use_column_width=True)
