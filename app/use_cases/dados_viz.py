from app.frameworks.banco_de_dados import BancoDeDados
import pandas as pd


class DadosVisualizacao:

    def __init__(self):
        self.banco_de_dados = BancoDeDados()

    
    def obter_valores_agrupados(self):
        dados_agrupados = self.banco_de_dados.obter_visao_mes()
        df_agrupados = pd.DataFrame(
            dados_agrupados,
            columns=['Usuario', 'Mês da compra', 'Categoria', 'Tipo de lançamento', 'Valor Total']
            )
        return df_agrupados
    