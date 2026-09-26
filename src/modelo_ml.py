import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

print("Iniciando a preparação para o Machine Learning...")

# 1. Carregar a base de dados tratada
df = pd.read_csv("dados_dengue_tratados.csv")
print(f"Total de registros carregados: {len(df)}")

# 2. Selecionar colunas preditoras (features) e o alvo (target)
# Vamos tentar prever a 'classi_fin' com base em dados demográficos e clínicos
colunas_features = ["cs_sexo", "cs_gestant", "cs_raca", "cs_escol_n", "evolucao"]

# Remover linhas que tenham valores nulos nessas colunas para evitar erros no modelo
df_ml = df.dropna(subset=colunas_features + ["classi_fin"]).copy()

# Converter variáveis categóricas em variáveis numéricas (One-Hot Encoding) para o algoritmo entender
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

    # 5. Fazer previsões com os dados de teste
    previsoes = modelo.predict(X_teste)

    # 6. Avaliar o desempenho do modelo
    acuracia = accuracy_score(y_teste, previsoes)
    print(f"\n===== RESULTADO DO MODELO =====")
    print(f"Acurácia (Precisão geral): {acuracia * 100:.2f}%")
else:
    print("Ainda não há registros suficientes na amostra atual para treinar o modelo com segurança. Vamos precisar expandir o limite da API na próxima etapa.")