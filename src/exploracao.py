import requests
import pandas as pd

# Endereço da API
url = "https://apidadosabertos.saude.gov.br/arboviroses/dengue"

# Parâmetros da consulta
parametros = {
    "nu_ano": "2024",
    "limit": 100,
    "offset": 0
}

# Consulta à API
resposta = requests.get(url, params=parametros)

print("Status da API:", resposta.status_code)

# Transformação dos dados em DataFrame
dados = resposta.json()
df = pd.DataFrame(dados["dengue"])

print("\nQuantidade de registros:", len(df))
print("Quantidade de variáveis:", len(df.columns))

# --------------------------------------------------
# LISTA DE VARIÁVEIS
# --------------------------------------------------

print("\n===== VARIÁVEIS DISPONÍVEIS =====")

for numero, coluna in enumerate(df.columns, start=1):
    print(f"{numero:3} - {coluna}")

# --------------------------------------------------
# PRIMEIROS REGISTROS
# --------------------------------------------------

print("\n===== PRIMEIROS REGISTROS =====")
print(df.head())

# --------------------------------------------------
# TIPOS DOS DADOS
# --------------------------------------------------

print("\n===== TIPOS DOS DADOS =====")
print(df.dtypes)

# --------------------------------------------------
# QUALIDADE DOS DADOS
# --------------------------------------------------

print("\n===== QUALIDADE DOS DADOS =====")

qualidade = pd.DataFrame({
    "preenchidos": df.notna().sum(),
    "vazios": df.isna().sum()
})

qualidade["percentual_preenchido"] = (
    qualidade["preenchidos"] / len(df) * 100
).round(2)

qualidade = qualidade.sort_values(
    by="percentual_preenchido",
    ascending=False
)

print(qualidade)
# --------------------------------------------------
# RESUMO DA QUALIDADE DOS DADOS
# --------------------------------------------------

print("\n===== RESUMO DA QUALIDADE =====")

total_variaveis = len(qualidade)

variaveis_100 = (qualidade["percentual_preenchido"] == 100).sum()
variaveis_parciais = (
    (qualidade["percentual_preenchido"] > 0) &
    (qualidade["percentual_preenchido"] < 100)
).sum()
variaveis_0 = (qualidade["percentual_preenchido"] == 0).sum()

print("Total de variáveis:", total_variaveis)
print("Variáveis 100% preenchidas:", variaveis_100)
print("Variáveis parcialmente preenchidas:", variaveis_parciais)
print("Variáveis 0% preenchidas:", variaveis_0)

print("\n===== VARIÁVEIS 100% PREENCHIDAS =====")
print(
    qualidade[
        qualidade["percentual_preenchido"] == 100
    ].index.tolist()
)

print("\n===== VARIÁVEIS PARCIALMENTE PREENCHIDAS =====")
print(
    qualidade[
        (qualidade["percentual_preenchido"] > 0) &
        (qualidade["percentual_preenchido"] < 100)
    ].index.tolist()
)

print("\n===== VARIÁVEIS 0% PREENCHIDAS =====")
print(
    qualidade[
        qualidade["percentual_preenchido"] == 0
    ].index.tolist()
)
print("\n===== FREQUÊNCIA DAS PRINCIPAIS VARIÁVEIS =====")

variaveis_interesse = [
    "cs_sexo",
    "cs_gestant",
    "cs_raca",
    "cs_escol_n",
    "sg_uf",
    "classi_fin",
    "criterio",
    "tpautocto",
    "evolucao"
]

for coluna in variaveis_interesse:
    print(f"\n--- {coluna} ---")
    print(df[coluna].value_counts(dropna=False))