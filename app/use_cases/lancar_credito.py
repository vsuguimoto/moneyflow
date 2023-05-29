from app.frameworks.banco_de_dados import BancoDeDados
from app.entities.lancamento import Lancamento

class LancarCreditoUseCase:

    def __init__(self, banco_de_dados: BancoDeDados):
        self.banco_de_dados = banco_de_dados

    def executar(self, nome, valor, categoria_id:int):
        self.banco_de_dados.inserir_lancamento(nome=nome, tipo='C', valor=valor, categoria_id=categoria_id)
        self.banco_de_dados.fechar_conexao()