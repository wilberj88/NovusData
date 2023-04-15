import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Data", page_icon="⚛️")

st.title('Novus Data ⚛️')
st.header("Tecnología Interoperable para Gobernar tus Datos al instante ⚡")

st.write("Configura y disfruta ahora ⏱️")

st.markdown(
  """
  - 🗣️ _    Titularidad
  - ♻️ _    Ciclo de Vida
  - 🏗️ _     Arquitectura
  - 🧮 _     Modelación
  - ⏲️ _     Operación
  - 🛂 _     Seguridad
  - 🚫 _     Privacidad
  - 🤝 _     Conciliación
  - 💡 _     Referentes
  - 🌊 _     Lago
  - ⚠️ _     Elementos Críticos
  - ℹ️ _     Metadata
  - ✅ _     Calidad
  - 🔄 _     Integración
  - ✝️ _     Políticas
  - ▶️ _     Estándares
  - 🔁 _     Procesos
  
  DISFRUTA TU ECOSISTEMA INTEROPERABLE AHORA 🕰
  """
)


if st.button('Activa tu plan anual de Gobernanza de Datos'):    
        st.title('Tenemos un contrato 📜  personalizado 🎯 a tu diagnóstico 🔎 ')
        st.text_input("Incorpore su firma si está de acuerdo con las condiciones")

        st.text_input("Incorpore su correo electrónico para envío de factura")
        st.write('Gracias por confiar en los servicios de Novus Datos ⚛️')
        
