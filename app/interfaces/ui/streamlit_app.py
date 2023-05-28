import streamlit as st 
from app.interfaces.controllers.categoria_controller import CategoriaController
from app.frameworks.banco_de_dados import BancoDeDados


banco_de_dados = BancoDeDados('MoneyFlow.db')

def run_app():
    st.markdown('# 💸 Money Flow')

     # Obtenha o nome da categoria a partir do usuário
    nome = st.text_input("Nome da Categoria")

    # Crie uma instância do controlador de categorias
    categoria_controller = CategoriaController(banco_de_dados)

    # Verifique se o usuário clicou no botão "Criar"
    if st.button("Criar"):
        if nome:
            # Chame o método do controlador para criar a categoria
            resultado = categoria_controller.criar_categoria(nome)
            st.success(f"Categoria criada com sucesso: {resultado}")
        else:
            st.error("Por favor, insira um nome para a categoria.")

    pass

