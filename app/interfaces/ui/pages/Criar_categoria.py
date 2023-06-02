from app.interfaces.controllers.categoria_controller import CategoriaController

from st_pages import Page, Section, show_pages_from_config, add_page_title
import streamlit as st

add_page_title()
show_pages_from_config()

st.header('Criar categoria')
controlador_categoria = CategoriaController()
CATEGORIA = st.text_input('Digite o nome da nova categoria')

if st.button('Criar'):
    controlador_categoria.criar_categoria(CATEGORIA)