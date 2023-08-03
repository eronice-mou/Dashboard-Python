import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.colored_header import colored_header
#from streamlit_extras.metric_cards import style_metric_cards


# Configuração do nome da página
st.set_page_config(
    page_title='Dashboard',
    page_icon=':bar_chart:',
    layout='wide'
)
st.header(':bar_chart: Dashboard')
st.markdown("---")

st.sidebar.image('Logo.png')
st.sidebar.title(':chart_with_downwards_trend: Menu')

menu = st.sidebar.selectbox(' ', ['Selecionar', 'Login', 'Processo produtivo', 'Dashboard'])

if menu == 'Login':
    st.title('Login')

    user_name = st.text_input('Usuário')
    password = st.text_input('Password', type='password')

    usuario = st.selectbox('Selecionar usuário', ['Selecionar', 'Usuário 1', 'Usuário 2', 'Usuário 3', 'Usuário 4', 'Usuário 5'])

    st.checkbox('Login')

#--COMEÇo-------LOGIN----------------------------------------------------------------------
# Selecionar modelo da placa
st.sidebar.header(':chart_with_downwards_trend: Modelo da placa')
modelo_placa = st.sidebar.selectbox(' ', ['Selecionar', 'Modelo X', 'Modelo Y', 'Modelo Z'])

# Gráficos para o Modelo X -------------------------------------------------------------------------------
col1, col2 = st.columns(2, gap='medium')
if modelo_placa == 'Modelo X':

    qnt_pecas_hora = st.sidebar.checkbox('Quantidade de peças produzidas por hora')
    qnt_pecas_dia = st.sidebar.checkbox('Quantidade de peças produzidas ao dia')
    qnt_ordem_producao = st.sidebar.checkbox('Quantidade de peças produzidas do total da ordem de produção')

    


    # Opção quantidade de peças produzidas por hora
    if qnt_pecas_hora:

        with col1:

            opcao1 = st.checkbox('Visualizar por Tebela X')
            if opcao1:
                st.write('Você escolheu visualizar por Tabela')

            colored_header(
                label="Quantidade de peças produzidas por hora",
                description=" ",
                color_name="violet-70",
            )

            chart_data = pd.DataFrame(
                np.random.randn(20, 2),
                columns=['a', 'b'])
            st.line_chart(chart_data)
    


    # Opção quantidade de peças produzidas por dia
    if qnt_pecas_dia:
        
        with col2:

            opcao2 = st.checkbox('Visualizar por Tebela Y')
            if opcao2:
                st.write('Você escolheu visualizar por Tabela')

            colored_header(
                label="Quantidade de peças produzidas ao dia",
                description=" ",
                color_name="violet-70",
            )

            chart_data = pd.DataFrame(
                np.random.randn(20, 2),
                columns=['a', 'b'])
            st.line_chart(chart_data)

    # Quantidade de peças produzidas do total da ordem de produção
    if qnt_ordem_producao:

        opcao3 = st.checkbox('Visualizar por Tebela Z')
        if opcao3:
            st.write('Você escolheu visualizar por Tabela')

        colored_header(
            label="Quantidade de peças produzidas do total da ordem de produção",
            description=" ",
            color_name="violet-70",
        )
        st.write('Quantidade de peças produzidas do total da ordem de produção')
        chart_data = pd.DataFrame(
            np.random.randn(20, 2),
            columns=['a', 'b'])
        st.line_chart(chart_data)
        st.markdown("---")



# Gráficos para modelo Y -------------------------------------------------------------------------------
elif modelo_placa == 'Modelo Y':
    st.title('Modelo Y')
    qnt_pecas_hora = st.sidebar.checkbox('Quantidade de peças produzidas por hora')
    qnt_pecas_dia = st.sidebar.checkbox('Quantidade de peças produzidas ao dia')
    qnt_ordem_producao = st.sidebar.checkbox('Quantidade de peças produzidas do total da ordem de produção')


# Gráficos para modelo Z -------------------------------------------------------------------------------
elif modelo_placa == 'Modelo Z':
    st.title('Modelo Z')
    qnt_pecas_hora = st.sidebar.checkbox('Quantidade de peças produzidas por hora')
    qnt_pecas_dia = st.sidebar.checkbox('Quantidade de peças produzidas ao dia')
    qnt_ordem_producao = st.sidebar.checkbox('Quantidade de peças produzidas do total da ordem de produção')



# Defeitos --------------------------------------------------------------------------------------------

st.sidebar.markdown("---")
st.sidebar.header(':chart_with_downwards_trend: Visualizar defeitos')

defeito1 = st.sidebar.checkbox('Defeito por marcação a laser')
defeito2 = st.sidebar.checkbox('Defeito por orientação da placa')
defeito3 = st.sidebar.checkbox('Defeito por placa errada')
defeito4 = st.sidebar.checkbox('Defeito por pallet incorreto')
defeito5 = st.sidebar.checkbox('Defeito por pallet com orientação incorreta')


col1, col2, col3, col4, col5 = st.columns(5, gap='medium')

with col1:
    if defeito1:
        st.markdown('#### Defeito por marcação a laser ####')
        st.markdown('### 500 ###')

with col2:
    if defeito2:
        st.markdown('#### Defeito por orientação da placa ####')
        st.markdown('### 750 ###')

with col3:
    if defeito3:
        st.markdown('#### Defeito por placa errada ####')
        st.markdown('### 920 ###')

with col4:
    if defeito4:
        st.markdown('#### Defeito por pallet incorreto ####')
        st.markdown('### 150 ###')

with col5:
    if defeito5:
        st.markdown('#### Defeito por pallet com orientação incorreta ####')
        st.markdown('### 300 ###')



# Informações de produção --------------------------------------------------------------------
st.sidebar.markdown("---")
tempo_medio = st.sidebar.checkbox('Tempo médio de produção de uma placa')
numero_de_paradas = st.sidebar.checkbox('Número de paradas do equipamento')
tempo_de_parada = st.sidebar.checkbox('Tempo de parada do equipamento')
ordem_de_producao = st.sidebar.checkbox('Ordem de produção')

col1, col2, col3, col4, col5 = st.columns(5, gap='medium')
with col1:
    if tempo_medio:
        st.markdown('#### Tempo médio de produção de uma placa ####')
        st.markdown('### 920 ###')


with col2:
    if numero_de_paradas:
        st.markdown('#### Número de paradas do equipamento ####')
        st.markdown('### 750 ###')


with col3:
    if tempo_de_parada:
        st.markdown('#### Tempo de parada do equipamento ####')
        st.markdown('### 150 ###')


with col4:
    if ordem_de_producao:
        st.markdown('#### Ordem de produção ####')
        st.markdown('### 300 ###')

with col5:
    if defeito5:
        st.markdown(' ')
