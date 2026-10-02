import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# CARREGANDO OS DADOS TRATADOS
# ==========================================

arquivo = "dados/dengue_tratado.csv"

df = pd.read_csv(arquivo)


print("===== GERAÇÃO DOS GRÁFICOS =====")


# ==========================================
# 1. CASOS POR SEXO
# ==========================================

sexo = df["cs_sexo"].value_counts()

sexo.index = sexo.index.map({
    "F": "Feminino",
    "M": "Masculino"
})

plt.figure(figsize=(8, 5))

sexo.plot(kind="bar")

plt.title("Casos de Dengue por Sexo")
plt.xlabel("Sexo")
plt.ylabel("Quantidade de casos")

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("dados/grafico_sexo.png")

plt.show()


# ==========================================
# 2. CLASSIFICAÇÃO FINAL
# ==========================================

classificacao = df["classi_fin"].value_counts().sort_index()

plt.figure(figsize=(8, 5))

classificacao.plot(kind="bar")

plt.title("Distribuição da Classificação Final")
plt.xlabel("Código da classificação")
plt.ylabel("Quantidade de casos")

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("dados/grafico_classificacao.png")

plt.show()


# ==========================================
# 3. EVOLUÇÃO DOS CASOS
# ==========================================

evolucao = df["evolucao"].value_counts().sort_index()

plt.figure(figsize=(8, 5))

evolucao.plot(kind="bar")

plt.title("Distribuição da Evolução dos Casos")
plt.xlabel("Código da evolução")
plt.ylabel("Quantidade de casos")

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("dados/grafico_evolucao.png")

plt.show()


# ==========================================
# 4. FREQUÊNCIA DOS SINTOMAS
# ==========================================

sintomas = [
    "febre",
    "mialgia",
    "cefaleia",
    "exantema",
    "vomito",
    "nausea",
    "artralgia"
]

quantidades = []

for sintoma in sintomas:
    quantidade = df[sintoma].notna().sum()
    quantidades.append(quantidade)


plt.figure(figsize=(10, 6))

plt.bar(sintomas, quantidades)

plt.title("Registros Disponíveis por Sintoma")
plt.xlabel("Sintoma")
plt.ylabel("Quantidade de registros")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("dados/grafico_sintomas.png")

plt.show()


# ==========================================
# FIM
# ==========================================

print("\nGráficos gerados com sucesso!")

print("\nArquivos criados:")
print("- dados/grafico_sexo.png")
print("- dados/grafico_classificacao.png")
print("- dados/grafico_evolucao.png")
print("- dados/grafico_sintomas.png")