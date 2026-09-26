import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar os dados tratados que geramos no passo anterior
print("Carregando base de dados tratada...")
df = pd.read_csv("dados_dengue_tratados.csv")

print(f"Total de registros carregados para visualização: {len(df)}")

# Configurar o estilo básico dos gráficos
plt.style.use('ggplot')

# --------------------------------------------------
# 2. GRÁFICO 1: Distribuição de Casos por Sexo (cs_sexo)
# --------------------------------------------------
if "cs_sexo" in df.columns:
    plt.figure(figsize=(8, 5))
    
    # Contagem de registros por sexo (substituindo códigos por rótulos amigáveis se necessário)
    contagem_sexo = df["cs_sexo"].value_counts()
    
    contagem_sexo.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Distribuição de Casos de Dengue por Sexo')
    plt.xlabel('Sexo')
    plt.ylabel('Quantidade de Notificações')
    plt.xticks(rotation=0)
    plt.tight_layout()
    
    # Salvar a imagem do gráfico
    plt.savefig('grafico_casos_sexo.png')
    print("Gráfico 'grafico_casos_sexo.png' gerado com sucesso!")
    plt.close()

# --------------------------------------------------
# 3. GRÁFICO 2: Distribuição por Evolução do Caso (evolucao)
# --------------------------------------------------
if "evolucao" in df.columns:
    plt.figure(figsize=(8, 5))
    
    contagem_evolucao = df["evolucao"].value_counts()
    
    contagem_evolucao.plot(kind='pie', autopct='%1.1f%%', startangle=90, cmap='Set3')
    plt.title('Evolução dos Casos de Dengue')
    plt.ylabel('') # Remove o rótulo do eixo y no gráfico de pizza
    plt.tight_layout()
    
    # Salvar a imagem do gráfico
    plt.savefig('grafico_evolucao_casos.png')
    print("Gráfico 'grafico_evolucao_casos.png' gerado com sucesso!")
    plt.close()

print("\nProcesso de visualização finalizado! Verifique as imagens geradas na pasta do projeto.")