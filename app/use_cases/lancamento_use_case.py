from app.frameworks.banco_de_dados import BancoDeDados
from app.entities.lancamento import Lancamento

class LancamentoUseCase:
    
    def __init__(self) -> None:
        self.banco_de_dados = BancoDeDados()
        
    
    def criar_lancamento(self, lancamento: Lancamento) -> None:
        self.banco_de_dados.criar_lancamento(
            nome=lancamento.nome,
            valor=lancamento.valor,
            tipo=lancamento.tipo,
            data_compra=lancamento.data_compra,
            categoria_id=lancamento.categoria_id,
            pessoa_id=lancamento.pessoa_id
        )
        