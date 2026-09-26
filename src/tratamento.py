import requests
import pandas as pd

# 1. Requisição dos dados da API (mesma base inicial)
url = "https://apidadosabertos.saude.gov.br/arboviroses/dengue"
parametros = {
    "nu_ano": "2024",
    "limit": 1000,  # Aumentamos um pouco o limite para ter uma amostra maior para análise
    "offset": 0
}

print("Baixando dados da API do Ministério da Saúde...")
resposta = requests.get(url, params=parametros)

if resposta.status_code == 200:
    dados = resposta.json()
    df = pd.DataFrame(dados["dengue"])
    print(f"Dados carregados com sucesso! Total de registros: {len(df)}")
else:
    print("Erro ao acessar a API:", resposta.status_code)
    exit()

# --------------------------------------------------
# 2. SELEÇÃO E LIMPEZA DE COLUNAS RELEVANTES
# --------------------------------------------------
# Selecionamos apenas as colunas que fazem sentido para o nosso escopo de análise
colunas_interesse = [
    "nu_ano", "sg_uf", "id_muni_not", "cs_sexo", 
    "cs_gestant", "cs_raca", "cs_escol_n", 
    "classi_fin", "evolucao", "tpautocto"
]

# Garantir que pegamos apenas colunas que realmente existem no DataFrame
colunas_existentes = [col for col in colunas_interesse if col in df.columns]
df_analise = df[colunas_existentes].copy()

# --------------------------------------------------
# 3. TRATAMENTO DE VALORES NULOS E TIPOS
# --------------------------------------------------
print("\nIniciando tratamento dos dados...")

# Exemplo: Preencher dados categóricos vazios com a categoria 'IGNORADO' ou 'NA'
if "cs_sexo" in df_analise.columns:
    df_analise["cs_sexo"] = df_analise["cs_sexo"].fillna("IGNORADO")

if "evolucao" in df_analise.columns:
    df_analise["evolucao"] = df_analise["evolucao"].fillna("IGNORADO")

# Remover linhas duplicadas se houver
antes_dup = len(df_analise)
df_analise = df_analise.drop_duplicates()
print(f"Removidas {antes_dup - len(df_analise)} linhas duplicadas.")

# --------------------------------------------------
# 4. EXPORTAÇÃO DA BASE TRATADA
# --------------------------------------------------
# Salvamos um arquivo CSV limpo para facilitar a criação dos gráficos na próxima etapa
arquivo_saida = "dados_dengue_tratados.csv"
df_analise.to_csv(arquivo_saida, index=False, encoding="utf-8-sig")

print(f"\nDados tratados salvos com sucesso no arquivo: {arquivo_saida}")
print("\nPrévia dos dados tratados:")
print(df_analise.head())