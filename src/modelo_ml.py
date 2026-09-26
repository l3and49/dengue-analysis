import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print("Iniciando a preparação e análise de Machine Learning...")

# 1. Carregar a base de dados tratada
df = pd.read_csv("dados_dengue_tratados.csv")
print(f"Total de registros carregados: {len(df)}")

# 2. Selecionar colunas preditoras (features) e o alvo (target)
colunas_features = ["cs_sexo", "cs_gestant", "cs_raca", "cs_escol_n", "evolucao"]

# Remover linhas com valores nulos nessas colunas
df_ml = df.dropna(subset=colunas_features + ["classi_fin"]).copy()

# Converter variáveis categóricas em numéricas (One-Hot Encoding)
X = pd.get_dummies(df_ml[colunas_features], drop_first=True)
y = df_ml["classi_fin"]

print(f"Registros válidos para treino após limpeza: {len(X)}")

if len(X) > 10:
    # 3. Dividir os dados em treino (80%) e teste (20%)
    X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. Criar e treinar o modelo de Classificação (Random Forest)
    print("Treinando o modelo de Machine Learning (Random Forest)...")
    modelo = RandomForestClassifier(random_state=42)
    modelo.fit(X_treino, y_treino)

    # 5. Fazer previsões e avaliar
    previsoes = modelo.predict(X_teste)
    acuracia = accuracy_score(y_teste, previsoes)
    print(f"\n===== RESULTADO DO MODELO =====")
    print(f"Acurácia (Precisão geral): {acuracia * 100:.2f}%")

    # 6. NOVIDADE: Extrair a Importância das Variáveis (Feature Importance)
    print("\nCalculando a importância das variáveis para o modelo...")
    importancias = modelo.feature_importances_
    nomes_colunas = X.columns

    # Criar um DataFrame para organizar
    df_importancia = pd.DataFrame({
        'Variavel': nomes_colunas,
        'Importancia': importancias
    }).sort_values(by='Importancia', ascending=True) # Ordem crescente para plotar bonito horizontalmente

    # 7. Gerar o Gráfico de Importância
    plt.figure(figsize=(10, 6))
    plt.barh(df_importancia['Variavel'], df_importancia['Importancia'], color='teal')
    plt.xlabel('Grau de Importância')
    plt.ylabel('Variáveis / Características')
    plt.title('Importância das Variáveis no Modelo de Random Forest (Dengue)')
    plt.tight_layout()

    # Salvar o gráfico como imagem
    nome_arquivo = 'grafico_importancia.png'
    plt.savefig(nome_arquivo)
    print(f"Gráfico '{nome_arquivo}' gerado e salvo com sucesso na raiz do projeto!")
    
else:
    print("Ainda não há registros suficientes na amostra atual para treinar o modelo.")