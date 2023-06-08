from app.interfaces.controllers.lancamento_controller import LancamentoController
from app.interfaces.controllers.categoria_controller import CategoriaController
from app.interfaces.controllers.pessoa_controller import PessoaController
from st_pages import show_pages_from_config
from streamlit_extras.app_logo import add_logo


import time

import streamlit as st 



def lancamentos():
    show_pages_from_config()
    add_logo('app/interfaces/ui/logo/logo.png')
    st.header('Money flow')

    ABAS = st.tabs(['Lançamento', 'Gerenciar pessoas', 'Gerenciar categorias'])

    controlador_lancamento = LancamentoController()
    controlador_categoria = CategoriaController()
    controlador_pessoa =  PessoaController()

    ######################
    # Aba de lançamentos #
    ######################
    with ABAS[0]:
        

        NOME_LANCAMENTO = st.text_input('Nome do lançamento')

        COLUNAS = st.columns(2)
        with COLUNAS[0]:
            VALOR = st.number_input(label='Valor em R$',min_value=0.01)
            DATA_LANCAMENTO = st.date_input('Data do lançamento')
            
            
        with COLUNAS[1]:
            lista_categorias = controlador_categoria.obter_categoria()
            lista_pessoas = controlador_pessoa.obter_pessoas()

            if len(lista_categorias) == 0:
                st.write('Categoria')
                st.write('Nenhuma categoria cadastrada, use a aba "Gerenciar categorias" para criar uma nova')
            
            else:
                CATEGORIA_ID = st.selectbox(
                    label='Categoria',
                    options=lista_categorias.keys(),
                    format_func=lambda x: lista_categorias[x]
                    )
                
                TIPO = st.selectbox(
                    label='Crédito ou Débito',
                    options=['C', 'D']
                    )

        if len(lista_pessoas) == 0:
            st.write('Pessoa')
            st.write('Nenhuma pessoa cadastrada, use a aba "Gerenciar pessoas" para cadastrar uma nova')
        else:
            PESSOA_ID = st.selectbox(
                label='Pessoa',
                options=lista_pessoas.keys(),
                format_func=lambda x: lista_pessoas[x]
                )


        if st.button('Lançar'):
            controlador_lancamento.lancamento(
                nome=NOME_LANCAMENTO,
                valor=VALOR,
                tipo=TIPO,
                data_compra=DATA_LANCAMENTO,
                pessoas_id=PESSOA_ID,
                categorias_id=CATEGORIA_ID
            )
            st.success('Sucesso!')

    ######################
    ### Aba de Pessoas ###
    ######################
    with ABAS[1]:

        new_user = st.text_input('Digite o nome da pessoa')

        if st.button('Criar nova pessoa'):
            controlador_pessoa.criar_pessoa(new_user)
            st.success(f'{new_user} cadastrado com sucesso!')
            time.sleep(3.5)
            st.experimental_rerun()
            
            

    ######################
    ## Aba de Categoria ##
    ######################
    with ABAS[2]:
        CATEGORIA = st.text_input('Digite o nome da nova categoria')

        if st.button('Criar categoria'):
            controlador_categoria.criar_categoria(CATEGORIA)
            st.success(f'Categoria "{CATEGORIA}" criada com sucesso!')
            time.sleep(3.5)
            st.experimental_rerun()


if __name__ == "__main__":
    lancamentos()
