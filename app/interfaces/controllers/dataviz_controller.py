from app.use_cases.dataviz_use_case import DataVizUseCase
from app.frameworks.banco_de_dados import BancoDeDados

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# TODO -> Expor filtros de data para todas as visualizações


class DataVizController:

    def __init__(self):
        self.dataviz_use_case = DataVizUseCase()
        self.dados_lancamento = self.obter_dados()
        self.meses_lancamento = self.dados_lancamento['Mês do lançamento'].sort_values().unique()
        
            
    def obter_dados(self):
        try:
            dados_viz = self.dataviz_use_case.obter_valores()
            return dados_viz
        
        except:
            return None
    
    def create_lineplot_express(self, mes_inicio, mes_fim):
        
        dados_periodo = self.dados_lancamento.query(f"(`Data do lançamento` >= '{mes_inicio}-01') & (`Data do lançamento` <= '{mes_fim}-31')")
        
        data_grouped = dados_periodo.groupby(['Mês do lançamento', 'Tipo de lançamento']).sum()[['Valor']].reset_index()
        
        fig = px.bar(
            data_frame=data_grouped,
            x='Mês do lançamento',
            y='Valor',
            color='Tipo de lançamento',
            barmode='group',
            text_auto=True,
        )
        
        fig.update_layout(
            title_text='Custos mensais',
            autosize=False,
            width=800,
            height=200,
            xaxis=dict(
                showline=True,
                showgrid=False,
                showticklabels=True,
                linecolor='rgb(204, 204, 204)',
                linewidth=2,
                dtick="M1",
                ),
            yaxis=dict(
                showgrid=False,
                showline=False,
                showticklabels=False,
                zeroline=False,
            ),
            showlegend=False
        )
        
        fig.update_traces(
            texttemplate="R$ %{y:.2f}",
        )
        
        fig._config['displayModeBar'] = False
        
        
        return fig
    
    
    def create_treemap_express(self, mes_inicio, mes_fim):
        
        data = self.dados_lancamento.query(f"(`Data do lançamento` >= '{mes_inicio}-01') & (`Data do lançamento` <= '{mes_fim}-31')")
        
        
        fig = px.treemap(
            data,
            path=[px.Constant('Geral'), 'Tipo de lançamento', 'Usuario', 'Categoria', 'Nome do lançamento'],
            values='Valor',
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