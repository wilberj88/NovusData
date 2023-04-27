import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Data", page_icon="⚛️")

st.title('Novus Data ⚛️')
st.header("Diagnóstico de Governanza de Datos al instante ⚡")

diccionario = st.selectbox("¿Tienes diccionario de datos?",
        ("No", "Sí", "En construcción", "Pendiente", "No sabe"),
    )


metadatos = st.selectbox("¿Tienes metadatos?",
        ("No", "Sí", "En construcción", "Pendiente", "No sabe"),
    )

ciclo_vida = st.selectbox("¿Tienes modelado el ciclo de vida de los datos?",
        ("No", "Sí", "En construcción", "Pendiente", "No sabe"),
    )

privacidad = st.selectbox("¿Tienes política de privacidad?",
        ("No", "Sí", "En construcción", "Pendiente", "No sabe"),
    )

categoria = st.radio(
        "Indica la categoría más avanzada👇 ",
        options=['Política', 'Proceso','Estándares'],
    )

if st.button('Calcular diagnóstico gratuito'):
        def render_basic_radar():
            option = {
                "title": {"text": "Diagnóstico actual con meta anual"},
                "legend": {"data": ["Actual", "Meta año 1"]},
                "radar": {
                    "indicator": [
                        {"name": "Diccionario", "max": 6500},
                        {"name": "Metadatos", "max": 16000},
                        {"name": "Políticas", "max": 30000},
                        {"name": "Estándares", "max": 38000},
                        {"name": "Procesos", "max": 52000},
                        {"name": "RoadMalGeneral", "max": 25000},
                    ]
                },
                "series": [
                    {
                        "name": "Reporte",
                        "type": "radar",
                        "data": [
                            {
                                "value": [2000, 10000, 20000, 3500, 15000, 11800],
                                "name": "Actual",
                            },
                            {
                                "value": [3500, 15000, 25000, 10800, 22000, 20000],
                                "name": "Meta año 1",
                            },
                        ],
                    }
                ],
            }
            st_echarts(option, height="500px")

        ST_RADAR_DEMOS = {
            "Radar: Basic Radar": (
                render_basic_radar,
                "https://echarts.apache.org/examples/en/editor.html?c=radar",
            ),
        }
        render_basic_radar()
