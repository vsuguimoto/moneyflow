from app.use_cases.pessoa_use_case import PessoaUseCase
from app.frameworks.banco_de_dados import BancoDeDados

class PessoaController:

    def __init__(self):
        self.banco_de_dados = BancoDeDados()
    

    def obter_pessoas(self) -> dict:
        pessoa_use_case = PessoaUseCase(self.banco_de_dados)
        nome_pessoas = pessoa_use_case.obter_pessoas_use_case()

        return nome_pessoas
    
    def criar_pessoa(self, nome: str):
        pessoa_use_case = PessoaUseCase(self.banco_de_dados)

        try:
            pessoa_use_case.criar_pessoa_use_case(nome)
        except Exception as e:
            return str(e)