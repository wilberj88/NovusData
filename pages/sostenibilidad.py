import streamlit as st
from streamlit_echarts import st_echarts
import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Data", page_icon="⚛️")

st.title('Novus Data ⚛️')
st.header("Diagnóstico de Sostenibilidad Empresarial al instante ⚡")

diccionario = st.selectbox("¿Tienes Protocolo de Medición de Emisiones?",
        ("No", "Sí", "En construcción", "Pendiente", "No sabe"),
    )


metadatos = st.selectbox("¿Tienes metadatos de las emisiones de los años anteriores?",
        ("No", "Sí", "En construcción", "Pendiente", "No sabe"),
    )

ciclo_vida = st.selectbox("¿Tienes modelado el ciclo de vida de todas las emisiones?",
        ("No", "Sí", "En construcción", "Pendiente", "No sabe"),
    )

privacidad = st.selectbox("¿Tienes política de mitigación de emisiones?",
        ("No", "Sí", "En construcción", "Pendiente", "No sabe"),
    )

seguridad = st.selectbox("¿Tienes política de adaptación?",
        ("No", "Sí", "En construcción", "Pendiente", "No sabe"),
    )

avanzada = st.radio(
        "Indica la categoría más avanzada ⬆",
        options=['Políticas', 'Procesos','Estándares'],
    )

retrasada = st.radio(
        "Indica la categoría más retrasada ⬇",
        options=['Políticas', 'Procesos','Estándares'],
    )

if st.button('Calcular diagnóstico gratuito'):
        def render_basic_radar():
            option = {
                "title": {"text": "Diagnóstico"},
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
        

        st.title('Hoja de Ruta de Implementación y Mejora de la Gobernanza de Datos 📆')
        st.markdown(
          """
          Componentes de la Estrategia de Gobernanza de Datos:
          - 📝 _    Titularidad de cada dato en cada etapa
          - 📝 _    Ciclo de Vida de todos los datos
          - 📆 _    Arquitectura de los sistemas de datos
          - 📍 _    Operación de los Datos
          - 📍 _    Seguridad de los Datos
          - 📍 _    Privacidad de los Datos
          - 📍 _    Conciliación de Pleitos en los Datos
          - 📍 _    Referentes de los Datos
          - 📍 _    Lago de los Datos
          - 📍 _    Elementos Críticos de los Datos
          - 📍 _    Calidad de los Datos
          - 📍 _    Integración de los Datos

          ANALIZA TU CALENDARIO AHORA: Políticas + Estándares + Procesos 🕰
          """
        )
        st.write('')
        def render_heatmap_cartesian():
            hours = [
                "12a",
                "1a",
                "2a",
                "3a",
                "4a",
                "5a",
                "6a",
                "7a",
                "8a",
                "9a",
                "10a",
                "11a",
                "12p",
                "1p",
                "2p",
                "3p",
                "4p",
                "5p",
                "6p",
                "7p",
                "8p",
                "9p",
                "10p",
                "11p",
            ]
            days = [
                "Saturday",
                "Friday",
                "Thursday",
                "Wednesday",
                "Tuesday",
                "Monday",
                "Sunday",
            ]

            data = [
                [0, 0, 5],
                [0, 1, 1],
                [0, 2, 0],
                [0, 3, 0],
                [0, 4, 0],
                [0, 5, 0],
                [0, 6, 0],
                [0, 7, 0],
                [0, 8, 0],
                [0, 9, 0],
                [0, 10, 0],
                [0, 11, 2],
                [0, 12, 4],
                [0, 13, 1],
                [0, 14, 1],
                [0, 15, 3],
                [0, 16, 4],
                [0, 17, 6],
                [0, 18, 4],
                [0, 19, 4],
                [0, 20, 3],
                [0, 21, 3],
                [0, 22, 2],
                [0, 23, 5],
                [1, 0, 7],
                [1, 1, 0],
                [1, 2, 0],
                [1, 3, 0],
                [1, 4, 0],
                [1, 5, 0],
                [1, 6, 0],
                [1, 7, 0],
                [1, 8, 0],
                [1, 9, 0],
                [1, 10, 5],
                [1, 11, 2],
                [1, 12, 2],
                [1, 13, 6],
                [1, 14, 9],
                [1, 15, 11],
                [1, 16, 6],
                [1, 17, 7],
                [1, 18, 8],
                [1, 19, 12],
                [1, 20, 5],
                [1, 21, 5],
                [1, 22, 7],
                [1, 23, 2],
                [2, 0, 1],
                [2, 1, 1],
                [2, 2, 0],
                [2, 3, 0],
                [2, 4, 0],
                [2, 5, 0],
                [2, 6, 0],
                [2, 7, 0],
                [2, 8, 0],
                [2, 9, 0],
                [2, 10, 3],
                [2, 11, 2],
                [2, 12, 1],
                [2, 13, 9],
                [2, 14, 8],
                [2, 15, 10],
                [2, 16, 6],
                [2, 17, 5],
                [2, 18, 5],
                [2, 19, 5],
                [2, 20, 7],
                [2, 21, 4],
                [2, 22, 2],
                [2, 23, 4],
                [3, 0, 7],
                [3, 1, 3],
                [3, 2, 0],
                [3, 3, 0],
                [3, 4, 0],
                [3, 5, 0],
                [3, 6, 0],
                [3, 7, 0],
                [3, 8, 1],
                [3, 9, 0],
                [3, 10, 5],
                [3, 11, 4],
                [3, 12, 7],
                [3, 13, 14],
                [3, 14, 13],
                [3, 15, 12],
                [3, 16, 9],
                [3, 17, 5],
                [3, 18, 5],
                [3, 19, 10],
                [3, 20, 6],
                [3, 21, 4],
                [3, 22, 4],
                [3, 23, 1],
                [4, 0, 1],
                [4, 1, 3],
                [4, 2, 0],
                [4, 3, 0],
                [4, 4, 0],
                [4, 5, 1],
                [4, 6, 0],
                [4, 7, 0],
                [4, 8, 0],
                [4, 9, 2],
                [4, 10, 4],
                [4, 11, 4],
                [4, 12, 2],
                [4, 13, 4],
                [4, 14, 4],
                [4, 15, 14],
                [4, 16, 12],
                [4, 17, 1],
                [4, 18, 8],
                [4, 19, 5],
                [4, 20, 3],
                [4, 21, 7],
                [4, 22, 3],
                [4, 23, 0],
                [5, 0, 2],
                [5, 1, 1],
                [5, 2, 0],
                [5, 3, 3],
                [5, 4, 0],
                [5, 5, 0],
                [5, 6, 0],
                [5, 7, 0],
                [5, 8, 2],
                [5, 9, 0],
                [5, 10, 4],
                [5, 11, 1],
                [5, 12, 5],
                [5, 13, 10],
                [5, 14, 5],
                [5, 15, 7],
                [5, 16, 11],
                [5, 17, 6],
                [5, 18, 0],
                [5, 19, 5],
                [5, 20, 3],
                [5, 21, 4],
                [5, 22, 2],
                [5, 23, 0],
                [6, 0, 1],
                [6, 1, 0],
                [6, 2, 0],
                [6, 3, 0],
                [6, 4, 0],
                [6, 5, 0],
                [6, 6, 0],
                [6, 7, 0],
                [6, 8, 0],
                [6, 9, 0],
                [6, 10, 1],
                [6, 11, 0],
                [6, 12, 2],
                [6, 13, 1],
                [6, 14, 3],
                [6, 15, 4],
                [6, 16, 0],
                [6, 17, 0],
                [6, 18, 0],
                [6, 19, 0],
                [6, 20, 1],
                [6, 21, 2],
                [6, 22, 2],
                [6, 23, 6],
            ]
            data = [[d[1], d[0], d[2] if d[2] != 0 else "-"] for d in data]

            option = {
                "tooltip": {"position": "top"},
                "grid": {"height": "50%", "top": "10%"},
                "xAxis": {"type": "category", "data": hours, "splitArea": {"show": True}},
                "yAxis": {"type": "category", "data": days, "splitArea": {"show": True}},
                "visualMap": {
                    "min": 0,
                    "max": 10,
                    "calculable": True,
                    "orient": "horizontal",
                    "left": "center",
                    "bottom": "15%",
                },
                "series": [
                    {
                        "name": "Punch Card",
                        "type": "heatmap",
                        "data": data,
                        "label": {"show": True},
                        "emphasis": {
                            "itemStyle": {"shadowBlur": 10, "shadowColor": "rgba(0, 0, 0, 0.5)"}
                        },
                    }
                ],
            }
            st_echarts(option, height="500px")


        ST_HEATMAP_DEMOS = {
            "Heatmap: Heatmap Cartesian": (
                render_heatmap_cartesian,
                "https://echarts.apache.org/examples/en/editor.html?c=heatmap-cartesian",
            ),
        }

        render_heatmap_cartesian()
        
        st.markdown(
          """
          Al finalizar la Hoja de Ruta de Gobernanza de Datos tendrás:
          - 📝 _    Certificación ISO Seguridad de los Datos
          - 📝 _    Certificación ISO Privacidad de los Datos
          - 📆 _    Certificación ISO Ética de los Datos

          EMPIEZA AHORA 🕰
          """
        )
