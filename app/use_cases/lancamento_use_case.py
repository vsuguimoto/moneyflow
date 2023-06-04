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
            categorias_id=lancamento.categorias_id,
            pessoas_id=lancamento.pessoas_id
        )

        self.banco_de_dados.criar_visao_mes()

    def remover_lancamento(self, lancamento_id) -> None:
        self.banco_de_dados.apagar_lancamento(
            lancamento_id=lancamento_id
        )