from app.entities.categoria import Categoria
from app.frameworks.banco_de_dados import BancoDeDados

import pandas as pd

class CategoriaUseCase:

    def __init__(self):
        self.banco_de_dados = BancoDeDados()
    
    def criar_categoria_use_case(self, nome_categoria):
        self.banco_de_dados.criar_categoria(nome=nome_categoria)
    
    def obter_categoria_use_case(self):
        categorias = self.banco_de_dados.obter_categoria()
        lista_categorias = pd.DataFrame(categorias)
        return lista_categorias
