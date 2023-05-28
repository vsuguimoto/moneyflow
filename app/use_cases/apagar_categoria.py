from app.frameworks.banco_de_dados import BancoDeDados

class ApagarCategoriaUseCase:
    def __init__(self, banco_de_dados: BancoDeDados):
        self.banco_de_dados = banco_de_dados
    
    def executar(self, categoria_id:int):
        self.banco_de_dados.apagar_categoria(cadegoria_id=categoria_id)
        self.banco_de_dados.fechar_conexao()