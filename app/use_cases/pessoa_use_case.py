from app.frameworks.banco_de_dados import BancoDeDados
from app.entities.pessoa import Pessoa

import pandas as pd

class PessoaUseCase:

    def __init__(self, banco_de_dados):
        self.banco_de_dados = banco_de_dados

    def criar_pessoa_use_case(self, nome):
        # Premissa:
        # Todos os nomes sempre serão em caixa alta
        nome_upper = nome.upper()
        pessoa = Pessoa(nome=nome_upper)
        self.banco_de_dados.criar_pessoa(nome)


    def obter_pessoas_use_case(self):
        nome_pessoas = self.banco_de_dados.obter_pessoa()
        pessoas = pd.DataFrame(nome_pessoas)
        return pessoas
    
