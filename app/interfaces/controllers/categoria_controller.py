from app.use_cases.criar_categoria import CriarCategoriaUseCase
from app.use_cases.apagar_categoria import ApagarCategoriaUseCase

class CategoriaController:
    def __init__(self, banco_de_dados):
        self.criar_categoria_use_case = CriarCategoriaUseCase(banco_de_dados)
        self.apagar_categoria_use_case = ApagarCategoriaUseCase(banco_de_dados)

    def criar_categoria(self, nome):
        try:
            categoria = self.criar_categoria_use_case.executar(nome)
            return categoria
        except Exception as e:
            return str(e)

    def apagar_categoria(self, categoria_id):
        try:
            self.apagar_categoria_use_case.executar(categoria_id)
            return "Categoria apagada com sucesso."
        except Exception as e:
            return str(e)