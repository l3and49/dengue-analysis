import pandas as pd


# ==========================================
# CARREGANDO OS DADOS TRATADOS
# ==========================================

arquivo = "dados/dengue_tratado.csv"

df = pd.read_csv(arquivo)

print("===== ANÁLISE DOS DADOS DE DENGUE =====")

print("\nQuantidade de registros:", len(df))
print("Quantidade de variáveis:", len(df.columns))


# ==========================================
# FUNÇÃO PARA MOSTRAR FREQUÊNCIAS E PERCENTUAIS
# ==========================================

def analisar_variavel(df, coluna):
    print(f"\n===== {coluna.upper()} =====")

    total = len(df)
    ausentes = df[coluna].isna().sum()
    validos = total - ausentes

    frequencias = df[coluna].value_counts(dropna=True)

    if validos > 0:
        for valor, quantidade in frequencias.items():
            percentual = (quantidade / validos) * 100
            print(f"{valor}: {quantidade} ({percentual:.2f}%)")

    percentual_ausentes = (ausentes / total) * 100

    print(f"Ausentes: {ausentes} ({percentual_ausentes:.2f}%)")


# ==========================================
# 1. CASOS POR SEXO
# ==========================================

print("\n===== CASOS POR SEXO =====")

total_validos = df["cs_sexo"].notna().sum()

for valor, quantidade in df["cs_sexo"].value_counts(dropna=True).items():

    if valor == "F":
        nome = "Feminino"
    elif valor == "M":
        nome = "Masculino"
    else:
        nome = valor

    percentual = (quantidade / total_validos) * 100

    print(f"{nome}: {quantidade} ({percentual:.2f}%)")

ausentes = df["cs_sexo"].isna().sum()
print(f"Ausentes: {ausentes}")


# ==========================================
# 2. RAÇA/COR
# ==========================================

analisar_variavel(df, "cs_raca")


# ==========================================
# 3. CLASSIFICAÇÃO FINAL
# ==========================================

analisar_variavel(df, "classi_fin")


# ==========================================
# 4. EVOLUÇÃO DOS CASOS
# ==========================================

analisar_variavel(df, "evolucao")


# ==========================================
# 5. HOSPITALIZAÇÃO
# ==========================================

analisar_variavel(df, "hospitaliz")


# ==========================================
# 6. SINTOMAS
# ==========================================

print("\n===== FREQUÊNCIA DOS SINTOMAS =====")

sintomas = [
    "febre",
    "mialgia",
    "cefaleia",
    "exantema",
    "vomito",
    "nausea",
    "artralgia"
]

for sintoma in sintomas:
    analisar_variavel(df, sintoma)


print("\n===== FIM DA ANÁLISE =====")