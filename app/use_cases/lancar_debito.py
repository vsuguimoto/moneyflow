from app.frameworks.banco_de_dados import BancoDeDados
from app.entities.lancamento import Lancamento

class LancarDebitoUseCase:

    def __init__(self):
        self.banco_de_dados = BancoDeDados()

    def executar(self, nome, valor, categoria_id:int):
        self.banco_de_dados.criar_lancamento(nome=nome, tipo='D', valor=valor, categoria_id=categoria_id)
        self.banco_de_dados.fechar_conexao()