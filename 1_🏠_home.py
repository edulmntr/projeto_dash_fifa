import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

st.markdown('# FIFA 2023 Official Dataset!⚽')
st.sidebar.markdown('Desenvolvido por Eduardo Monteiro')

btn = st.button("Acesse os dados no Keggle")

if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database")

st.markdown(
    '''
    Este é um extenso e detalhado conjunto de dados que mapeia a evolução dos jogadores de futebol nas populares edições do videogame FIFA,
    abrangendo do FIFA 17 até o FIFA 23. Ele funciona como um grande "catálogo" de futebol digital, contendo mais de **17.000 jogadores** únicos 
    e mais de 60 indicadores de performance (KPIs) para cada um. Estes dados incluem informações gerais (como nome, clube e nacionalidade) e, o mais importante, 
    todas as notas de habilidade dentro do jogo, como ritmo (pace), chute (shooting) e drible (dribbling).

    A principal utilidade deste dataset reside em sua relevância para a comunidade de esports e gamers.
    Com o crescente profissionalismo da cena competitiva do FIFA, a base de dados permite que analistas, jogadores e cientistas de dados 
    (Kagglers) estudem, comparem e avaliem o desempenho e o valor dos atletas de forma estatística. Ele é uma ferramenta poderosa para montar escalações ideais,
    rastrear a progressão de talentos ao longo dos anos e realizar análises preditivas sobre a performance dos jogadores no ambiente do jogo.
''')