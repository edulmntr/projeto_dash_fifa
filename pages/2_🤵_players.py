import streamlit as st

st.set_page_config(
    layout='wide',
    page_title='Players',
    page_icon='🏃‍♂️'
)

df_data = st.session_state["data"]

clubes = df_data["Club"].unique()
club = st.sidebar.selectbox("Clube", clubes)

df_players = df_data[(df_data["Club"] == club)]

players = df_players["Name"].unique()
player = st.sidebar.selectbox("Jogadores", players)

player_stats = df_data[df_data['Name'] == player].iloc[0]

st.image(player_stats['Photo'])
st.title(player_stats['Name'])

st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")
st.markdown(f"**Origem:** {player_stats['Nationality']}")

col1, col2, col3, col4 = st.columns(4)

col1.markdown(f"**Idade**: {player_stats['Age']}")
col2.markdown(f"**Altura**: {(player_stats['Height(cm.)'] / 100):.2f}")
col3.markdown(f"**Peso**: {(player_stats['Weight(lbs.)']/ 2.20462):.2f}")
st.divider()

st.subheader(f"Overall: {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

col1, col2, col3= st.columns(3)

col1.metric(label="Valor de Mercado", value=f"£{player_stats['Value(£)']:,}")
col2.metric(label="Salário", value=f"£{player_stats['Wage(£)']}")
col3.metric(label="Cláusula de Recisão", value=f"£{player_stats['Release Clause(£)']:,}")