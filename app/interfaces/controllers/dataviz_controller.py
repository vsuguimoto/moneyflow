from app.use_cases.dataviz_use_case import DataVizUseCase
from app.frameworks.banco_de_dados import BancoDeDados

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class DataVizController:

    def __init__(self):
        self.dataviz_use_case = DataVizUseCase()

    def __obter_dados(self):
        try:
            dados_viz = self.dataviz_use_case.obter_valores_agrupados()
            return dados_viz
        
        except:
            print('Tabela Inexistente')
    
    
    def create_treemap_express(self):
        
        data = self.__obter_dados()
        
        fig = px.treemap(
            data,
            path=[px.Constant('Geral'), 'Tipo de lançamento', 'Usuario', 'Categoria'],
            values='Valor total',
            maxdepth=2,
            
        )
        
        fig.update_layout(
            title_text='Treemap de Compras',
            autosize=False,
            width=800,
            height=600,
        )
        
        fig.update_traces(
            marker=dict(
                cornerradius=5
            ),
            root_color="lightgrey",
            texttemplate="%{label}<br>R$ %{value:.2f}",
            hovertemplate='<b>%{label}</b><br>Valor: R$%{value:.2f}<extra></extra>'
        )
        
        return fig