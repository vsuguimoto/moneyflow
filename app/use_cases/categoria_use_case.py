from app.entities.categoria import Categoria
from app.frameworks.banco_de_dados import BancoDeDados

import pandas as pd

class CategoriaUseCase:

    def __init__(self):
        self.banco_de_dados = BancoDeDados()
    
    def criar_categoria_use_case(self, nome_categoria):
        nome_upper = nome_categoria.upper()
        self.banco_de_dados.criar_categoria(nome=nome_upper)
    
    def obter_categoria_use_case(self):
        categorias = self.banco_de_dados.obter_categoria()
        try:
            lista_categorias = dict(categorias)
            return lista_categorias
        except:
            return None
