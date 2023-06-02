from app.interfaces.controllers.lancamento_controller import LancamentoController
from app.interfaces.controllers.categoria_controller import CategoriaController

from st_pages import Page, Section, show_pages_from_config, add_page_title
import streamlit as st

add_page_title()
show_pages_from_config()


st.header('Lançamento')

# TODO -> Criar status para o mês atual


COLUNAS = st.columns(2) 
with COLUNAS[0]:
    controlador_lancamento = LancamentoController()
    VALOR = st.number_input(label='Valor em R$',min_value=0.01)
with COLUNAS[1]:
    controlador_categoria = CategoriaController()
    lista_categorias = controlador_categoria.obter_categoria()
    CATEGORIA = st.selectbox(label='Categoria', options=lista_categorias)