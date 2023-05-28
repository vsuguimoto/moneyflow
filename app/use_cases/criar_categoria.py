from app.entities.categoria import Categoria
from app.frameworks.banco_de_dados import BancoDeDados

class CriarCategoriaUseCase:
    def __init__(self, banco_de_dados: BancoDeDados):
        self.banco_de_dados = banco_de_dados

    def executar(self, nome: str, descricao: str):
        categoria = Categoria(nome=nome, descricao=descricao)
        self.banco_de_dados.criar_categoria(categoria.nome, categoria.descricao)
        self.banco_de_dados.fechar_conexao()