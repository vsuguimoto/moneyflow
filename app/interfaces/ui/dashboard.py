from app.interfaces.controllers.dataviz_controller import DataVizController
from st_pages import show_pages_from_config
from streamlit_extras.app_logo import add_logo

import streamlit as st


show_pages_from_config()
add_logo('app/interfaces/ui/logo/logo.png', height=120)

st.header('MoneyFlow')

controlador_dataviz = DataVizController()
dados_dataviz = controlador_dataviz.obter_dados()

st.table(dados_dataviz)