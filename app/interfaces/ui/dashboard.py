from app.interfaces.controllers.dataviz_controller import DataVizController
from st_pages import show_pages_from_config
from streamlit_extras.app_logo import add_logo

import streamlit as st


def dashboard():
    show_pages_from_config()
    add_logo('app/interfaces/ui/logo/logo.png', height=120)

    st.header('MoneyFlow')
    
    if st.button('Atualizar'):
        st.experimental_rerun()

    controlador_dataviz = DataVizController()
    
    
    
    st.plotly_chart(controlador_dataviz.create_treemap_express())




if __name__ == "__main__":
    dashboard()
