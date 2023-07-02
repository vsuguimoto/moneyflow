from app.interfaces.controllers.dataviz_controller import DataVizController

from st_pages import show_pages_from_config
from streamlit_extras.app_logo import add_logo

import streamlit as st


def dashboard():
    show_pages_from_config()
    add_logo('app/interfaces/ui/logo/logo.png', height=120)
    

    st.header('Money flow')
    
    if st.button('Atualizar'):
        st.experimental_rerun()
    controlador_dataviz = DataVizController()

    mes_inicio, mes_fim = st.select_slider(
        label='Datas',
        options=controlador_dataviz.meses_lancamento,
        value=(controlador_dataviz.meses_lancamento[0],
               controlador_dataviz.meses_lancamento[-1])
    )
    
    st.plotly_chart(controlador_dataviz.create_lineplot_express(mes_inicio, mes_fim),
                    use_container_width=True,
                    config=dict(displayModeBar=False)
    )
    st.plotly_chart(controlador_dataviz.create_treemap_express(mes_inicio, mes_fim),
                    use_container_width=True,
                    config=dict(displayModeBar=False)
    )

colunas_metrica = st.columns(3)

with colunas_metrica[0]:
    creditos_totais = dados_dataviz.query('`Tipo de lançamento`== "C"')['Valor Total'].sum()
    st.metric('Créditos', f'R$ {creditos_totais:.2f}')

with colunas_metrica[1]:
    debitos_totais = dados_dataviz.query('`Tipo de lançamento`== "D"')['Valor Total'].sum()
    st.metric('Débitos', f'R$ {debitos_totais:.2f}')

with colunas_metrica[2]:
    st.metric('Líquido', f'R$ {creditos_totais - debitos_totais:.2f}')

st.table(dados_dataviz)
