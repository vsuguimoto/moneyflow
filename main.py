from app.interfaces.controllers.pessoa_controller import PessoaController
import streamlit as st
from st_pages import Page, Section, show_pages_from_config, add_page_title


show_pages_from_config()

st.header('# Money Flow')

st.write('Antes de iniciarmos, selecione o usuário:')

pessoa_control = PessoaController()
LISTA_PESSOAS = pessoa_control.obter_pessoas()

user = st.selectbox('Selecione o usuário', LISTA_PESSOAS)

cols = st.columns(9)
with cols[-1]:  
    usuario_selecionado = st.button('Login')

if usuario_selecionado:
    st.success('Sucesso!!')

st.markdown('---')

