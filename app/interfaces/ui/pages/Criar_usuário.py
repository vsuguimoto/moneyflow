from app.interfaces.controllers.pessoa_controller import PessoaController
from st_pages import Page, Section, show_pages_from_config, add_page_title

import streamlit as st

add_page_title()
show_pages_from_config()


st.write('Antes de iniciarmos, selecione o usuário:')

pessoa_control = PessoaController()

new_user = st.text_input('Digite seu nome:')

if st.button('Criar'):

    pessoa_control.criar_pessoa(new_user)