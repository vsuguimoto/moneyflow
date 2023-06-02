import streamlit as st 
from app.interfaces.controllers.categoria_controller import CategoriaController
from app.interfaces.controllers.lancamento_controller import LancamentoController
from app.interfaces.controllers.pessoa_controller import PessoaController
from app.frameworks.banco_de_dados import BancoDeDados



def selecionar_pessoa():

    st.markdown('# 💸 Money Flow')

    pessoa_controller = PessoaController()
    nome_pessoas = pessoa_controller.obter_pessoas()

    st.radio('Selecione o usuário:', nome_pessoas)

        