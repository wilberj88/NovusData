import streamlit as st

st.title('Diagnóstico de Governanza de Datos')

def render_basic_radar():
        option = {
                "title": {"text": "Transición energética"},
                "legend": {"data": ["Consumo Actual", "Consumo Óptimo"]},
                "radar": {
                    "indicator": [
                        {"name": "Agua", "max": 6500},
                        {"name": "Carbón", "max": 16000},
                        {"name": "Viento", "max": 30000},
                        {"name": "Sol", "max": 38000},
                        {"name": "Petróleo", "max": 52000},
                        {"name": "Gas", "max": 25000},
                    ]
                },
                "series": [
                    {
                        "name": "Consumo Actual Vs Óptimo",
                        "type": "radar",
                        "data": [
                            {
                                "value": [2000, 10000, 20000, 3500, 15000, 11800],
                                "name": "Consumo Actual",
                            },
                            {
                                "value": [3500, 15000, 25000, 10800, 22000, 20000],
                                "name": "Consumo Óptimo",
                            },
                        ],
                    }
                ],
            }
        st_echarts(option, height="500px")
    render_basic_radar()
