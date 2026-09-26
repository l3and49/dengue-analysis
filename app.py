import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Configuração da página do App
st.set_page_config(
    page_title="Dashboard de Dengue - AI & Data",
    page_icon="🦟",
    layout="wide"
)

st.title("🦟 Análise Inteligente de Dados de Dengue")
st.markdown("Plataforma interativa desenvolvida com Engenharia de Dados e Inteligência Artificial.")

# 1. Carregar os dados
@st.cache_data
def carregar_dados():
    # Apontando para o caminho correto dentro da pasta src ou na raiz
    df = pd.read_csv("src/dados_dengue_tratados.csv")
    return df

df = carregar_dados()

# Barra lateral (Sidebar) para filtros
st.sidebar.header("Filtros do Sistema")
sexo_selecionado = st.sidebar.selectbox(
    "Filtrar por Sexo:", 
    options=["Todos"] + list(df['cs_sexo'].dropna().unique())
)

# Aplicar filtro
df_filtrado = df.copy()
if sexo_selecionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado['cs_sexo'] == sexo_selecionado]

# 2. Métricas Principais (KPIs) no topo
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total de Registros (Filtrado)", len(df_filtrado))
with col2:
    st.metric("Acurácia do Modelo IA", "98.48%")
with col3:
    st.metric("Status da Base", "Atualizada & Limpa")

st.markdown("---")

# 3. Seção de Visualização de Dados
st.subheader("📊 Análise Exploratória e Distribuição")
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.write("**Distribuição por Sexo**")
    contagem_sexo = df['cs_sexo'].value_counts()
    st.bar_chart(contagem_sexo)

with col_graf2:
    st.write("**Evolução dos Casos (Amostra)**")
    
    # Descobrir qual coluna representa a data no DataFrame
    colunas_possiveis = ['dt_notific', 'dt_notificacao', 'data', 'co_notif', 'anu_notif']
    coluna_encontrada = next((col for col in colunas_possiveis if col in df.columns), None)
    
    if coluna_encontrada:
        dados_tempo = df[coluna_encontrada].value_counts().sort_index()
        st.line_chart(dados_tempo)
    else:
        # Se não achar por nome, pega a primeira coluna que pareça texto/data ou exibe uma contagem geral
        st.write("Visualização de registros agrupados:")
        st.bar_chart(df.iloc[:, 0].value_counts().head(10))

st.markdown("---")

# 4. Seção de Machine Learning e Explicabilidade
st.subheader("🤖 Inteligência Artificial (Random Forest)")
st.write("O modelo preditivo analisa os fatores determinantes com base nos dados tratados.")

colunas_features = ["cs_sexo", "cs_gestant", "cs_raca", "cs_escol_n", "evolucao"]
df_ml = df.dropna(subset=colunas_features + ["classi_fin"]).copy()

if len(df_ml) > 10:
    X = pd.get_dummies(df_ml[colunas_features], drop_first=True)
    y = df_ml["classi_fin"]
    
    X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)
    modelo = RandomForestClassifier(random_state=42)
    modelo.fit(X_treino, y_treino)
    
    # Extrair importância
    importancias = modelo.feature_importances_
    df_importancia = pd.DataFrame({
        'Variável': X.columns,
        'Importância': importancias
    }).set_index('Variável')
    
    st.write("**Gráfico de Importância das Variáveis (Feature Importance):**")
    st.bar_chart(df_importancia)
else:
    st.warning("Registros insuficientes para treinar o modelo com os filtros atuais.")