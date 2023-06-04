from app.interfaces.controllers.lancamento_controller import LancamentoController
from app.interfaces.controllers.categoria_controller import CategoriaController

from st_pages import Page, Section, show_pages_from_config, add_page_title
import streamlit as st

add_page_title()
show_pages_from_config()


st.header('Lançamento')

# TODO -> Criar status para o mês atual

controlador_lancamento = LancamentoController()
controlador_categoria = CategoriaController()

COLUNAS = st.columns(2)
with COLUNAS[0]:
    VALOR = st.number_input(label='Valor em R$',min_value=0.01)
    DATA_LANCAMENTO = st.date_input('Data do lançamento')
    
    
with COLUNAS[1]:
    lista_categorias = controlador_categoria.obter_categoria()
    CATEGORIA = st.selectbox(label='Categoria', options=lista_categorias)
    TIPO = st.selectbox('Crédito ou Débito', ['Crédito', 'Débito'])