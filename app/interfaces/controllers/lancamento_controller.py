from app.use_cases.lancamento_use_case import LancamentoUseCase
from app.entities.lancamento import Lancamento
from app.frameworks.banco_de_dados import BancoDeDados

class LancamentoController:

    def __init__(self):
        self.lancamentos = LancamentoUseCase()

    def lancamento(self, nome, valor, tipo, data_compra, categorias_id, pessoas_id):
        try:
            lancamento_atual = Lancamento(
                nome=nome,
                valor=valor,
                tipo=tipo,
                data_compra=data_compra,
                categorias_id=categorias_id,
                pessoas_id=pessoas_id
            )
            lancamento = self.lancamentos.criar_lancamento(lancamento_atual)
        
        except Exception as e:
            return str(e)
