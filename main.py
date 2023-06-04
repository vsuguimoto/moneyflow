from app.interfaces.controllers.pessoa_controller import PessoaController
import streamlit as st
from st_pages import Page, Section, show_pages_from_config, add_page_title


if 'usuario' not in st.session_state:
    st.session_state['usuario'] = None


show_pages_from_config()

st.header('# Money Flow')

if st.session_state['usuario'] == None:
    
    st.write('Antes de iniciarmos, selecione o usuário:')

    pessoa_control = PessoaController()
    LISTA_PESSOAS = pessoa_control.obter_pessoas()

    usuario = st.selectbox('Selecione o usuário', LISTA_PESSOAS)

    cols = st.columns(9)
    with cols[-1]:  
        usuario_selecionado = st.button('Login')

    if usuario_selecionado:
        st.session_state['usuario'] = usuario
        st.success('Sucesso!!')

    st.markdown('---')


else:
    # TODO -> Ir para página de Dashboards
    pass