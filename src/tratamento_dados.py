import requests
import pandas as pd


# URL da API
url = "https://apidadosabertos.saude.gov.br/arboviroses/dengue"

# Parâmetros da consulta
parametros = {
    "nu_ano": "2024",
    "limit": 1000,
    "offset": 0
}

# Consulta à API
resposta = requests.get(url, params=parametros)

print("Status da API:", resposta.status_code)

# Converte a resposta para JSON
dados = resposta.json()

# Cria o DataFrame original
df = pd.DataFrame(dados["dengue"])

print("Registros recebidos:", len(df))
print("Variáveis originais:", len(df.columns))


# Variáveis selecionadas para a análise
variaveis_selecionadas = [
    "dt_notific",
    "nu_ano",
    "sg_uf_not",
    "id_municip",
    "cs_sexo",
    "cs_gestant",
    "cs_raca",
    "cs_escol_n",
    "ano_nasc",
    "febre",
    "mialgia",
    "cefaleia",
    "exantema",
    "vomito",
    "nausea",
    "artralgia",
    "diabetes",
    "hipertensa",
    "hospitaliz",
    "classi_fin",
    "criterio",
    "tpautocto",
    "evolucao",
    "dt_obito",
    "dt_encerra"
]


# Cria o DataFrame tratado
df_tratado = df[variaveis_selecionadas].copy()




print("Variáveis após tratamento:", len(df_tratado.columns))
print("\nVariáveis selecionadas:")
print(df_tratado.columns.tolist())

print("\nPrimeiros registros:")
print(df_tratado.head())

print("\n===== VALORES AUSENTES =====")

ausentes = df_tratado.isna().sum()

percentual_ausentes = (
    df_tratado.isna().mean() * 100
).round(2)

resumo_ausentes = pd.DataFrame({
    "quantidade_ausentes": ausentes,
    "percentual_ausentes": percentual_ausentes
})

print(resumo_ausentes.sort_values(
    "percentual_ausentes",
    ascending=False
))

print("\n===== QUALIDADE DOS REGISTROS =====")

print("Total de registros:", len(df_tratado))

print("Registros duplicados:", df_tratado.duplicated().sum())

print(
    "Registros com pelo menos um valor ausente:",
    df_tratado.isna().any(axis=1).sum()
)

print(
    "Registros totalmente preenchidos:",
    df_tratado.notna().all(axis=1).sum()
)

print("\n===== TRATAMENTO DAS DATAS =====")

colunas_data = [
    "dt_notific",
    "dt_obito",
    "dt_encerra"
]

for coluna in colunas_data:
    df_tratado[coluna] = pd.to_datetime(
        df_tratado[coluna],
        errors="coerce"
    )

print(df_tratado[colunas_data].dtypes)

df_tratado["dias_ate_encerramento"] = (
    df_tratado["dt_encerra"] - df_tratado["dt_notific"]
).dt.days

print("\n===== TEMPO ATÉ O ENCERRAMENTO =====")
print(df_tratado["dias_ate_encerramento"].describe())

print("\n===== DATAS INCONSISTENTES =====")

datas_inconsistentes = df_tratado[
    df_tratado["dias_ate_encerramento"] < 0
]

print(
    "Registros com encerramento antes da notificação:",
    len(datas_inconsistentes)
)

print(
    datas_inconsistentes[
        ["dt_notific", "dt_encerra", "dias_ate_encerramento"]
    ].head(10)
)
print("\n===== REGISTROS DUPLICADOS =====")

duplicados = df_tratado[df_tratado.duplicated(keep=False)]

print("Quantidade de registros envolvidos:", len(duplicados))

print(duplicados)
print("\n===== DUPLICATAS EXATAS =====")

duplicados_exatos = df_tratado[
    df_tratado.duplicated(keep=False)
]

print("Quantidade de linhas envolvidas:", len(duplicados_exatos))
# Remove apenas duplicatas exatas
antes = len(df_tratado)

df_tratado = df_tratado.drop_duplicates().copy()

depois = len(df_tratado)

print("\n===== REMOÇÃO DE DUPLICATAS EXATAS =====")
print("Registros antes:", antes)
print("Registros removidos:", antes - depois)
print("Registros após tratamento:", depois)

print(
    duplicados_exatos[
        [
            "dt_notific",
            "sg_uf_not",
            "id_municip",
            "cs_sexo",
            "cs_gestant",
            "cs_raca",
            "cs_escol_n",
            "ano_nasc",
            "classi_fin",
            "criterio",
            "evolucao",
            "dt_encerra"
        ]
    ].sort_values(
        ["dt_notific", "id_municip", "ano_nasc"]
    )
)
print("\n===== POSSÍVEIS REPETIÇÕES POR PACIENTE/DATA =====")

chave = [
    "dt_notific",
    "id_municip",
    "cs_sexo",
    "ano_nasc"
]

repeticoes = df_tratado[
    df_tratado.duplicated(
        subset=chave,
        keep=False
    )
]

print("Registros com mesma combinação de data, município, sexo e ano de nascimento:")
print(len(repeticoes))

print(
    repeticoes[
        chave + [
            "cs_raca",
            "cs_escol_n",
            "classi_fin",
            "criterio",
            "evolucao",
            "dt_encerra"
        ]
    ].sort_values(chave)
)

print("\n===== SALVANDO DADOS TRATADOS =====")

df_tratado.to_csv(
    "dados/dengue_tratado.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Arquivo salvo em: dados/dengue_tratado.csv")