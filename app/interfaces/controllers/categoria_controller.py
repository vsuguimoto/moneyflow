from app.use_cases.criar_categoria import CriarCategoriaUseCase
from app.use_cases.apagar_categoria import ApagarCategoriaUseCase
from app.use_cases.categoria_use_case import CategoriaUseCase


class CategoriaController:
    def __init__(self):
        self.categoria_use_case = CategoriaUseCase()

    def criar_categoria(self, nome):
        try:
            categoria = self.categoria_use_case.criar_categoria_use_case(nome)
            return categoria
        except Exception as e:
            return str(e)

    def obter_categoria(self):
        try:
            categorias = self.categoria_use_case.obter_categoria_use_case()
            return categorias
        except Exception as e:
            return str(e)