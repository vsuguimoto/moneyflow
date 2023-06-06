from app.use_cases.dataviz_use_case import DataVizUseCase
from app.frameworks.banco_de_dados import BancoDeDados

class DataVizController:

    def __init__(self):
        self.dataviz_use_case = DataVizUseCase()

    def obter_dados(self):
        return self.dataviz_use_case.obter_valores_agrupados()
    
    