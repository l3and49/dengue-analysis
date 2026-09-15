import requests
import pandas as pd

url = "https://apidadosabertos.saude.gov.br/arboviroses/dengue"

parametros = {
    "nu_ano": "2024",
    "limit": 10,
    "offset": 0
}

resposta = requests.get(url, params=parametros)

print("Status:", resposta.status_code)
print("URL:", resposta.url)

dados = resposta.json()

df = pd.DataFrame(dados["dengue"])

print("\nDataFrame:")
print(df.head())

print("Tipo dos dados:", type(dados))
print("Chaves:", dados.keys())
print("Quantidade de registros:", len(dados["dengue"]))

primeiro_registro = dados["dengue"][0]

print("\nPrimeiro registro:")

print("\nAlguns campos do primeiro registro:")

print("Ano:", primeiro_registro["nu_ano"])
print("Data da notificação:", primeiro_registro["dt_notific"])
print("Município:", primeiro_registro["id_municip"])
print("UF:", primeiro_registro["sg_uf"])
print("Sexo:", primeiro_registro["cs_sexo"])
print("Ano de nascimento:", primeiro_registro["ano_nasc"])