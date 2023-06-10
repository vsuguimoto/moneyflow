from app.frameworks.banco_de_dados import BancoDeDados

from datetime import datetime
import pandas as pd

# TODO -> Criar GET de dados completos, revisar a necessidade do agrupamento
# TODO -> Criar use case para obter dados do slider

class DataVizUseCase:

    def __init__(self):
        self.banco_de_dados = BancoDeDados()

    
    def obter_valores_agrupados(self):
        dados_agrupados = self.banco_de_dados.obter_visao_mes()
        df_agrupados = pd.DataFrame(
            dados_agrupados,
            columns=['Usuario', 'Mês da compra', 'Categoria', 'Tipo de lançamento', 'Valor total']
            )
        
        df_agrupados['Tipo de lançamento'] = df_agrupados['Tipo de lançamento'].map({'C':'Crédito', 'D': 'Débito'})
        
        return df_agrupados
    
    def obter_valores(self):
        
        dados = self.banco_de_dados.obter_visao_geral()
        df_dados = pd.DataFrame(
            dados,
            columns=['Usuario', 'Data do lançamento', 'Nome do lançamento', 'Categoria', 'Tipo de lançamento', 'Valor']
        )
        df_dados['Tipo de lançamento'] = df_dados['Tipo de lançamento'].map({'C':'Crédito', 'D': 'Débito'})
        df_dados['Mês do lançamento'] = [datetime.strftime(data, '%Y-%m') for data in pd.to_datetime(df_dados['Data do lançamento'])]
        
        return df_dados
    
    
    