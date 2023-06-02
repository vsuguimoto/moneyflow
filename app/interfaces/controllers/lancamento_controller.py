from app.use_cases.lancar_credito import LancarCreditoUseCase
from app.use_cases.lancar_debito import LancarDebitoUseCase
from app.frameworks.banco_de_dados import BancoDeDados

class LancamentoController:

    def __init__(self):
        self.lancar_credito_use_case = LancarCreditoUseCase()
        self.lancar_debito_use_case = LancarDebitoUseCase()

    def lancar_credito(self, nome, valor, categoria_id):
        try:
            lancamento = self.lancar_credito_use_case.executar(nome=nome, valor=valor, categoria_id=categoria_id)
            return lancamento
        except Exception as e:
            return str(e)
    
    def lancar_debito(self, nome, valor, categoria_id):
        try:
            lancamento = self.lancar_debito_use_case.executar(nome=nome, valor=valor, categoria_id=categoria_id)
            return lancamento
        except Exception as e:
            return str(e)