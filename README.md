# Dengue Analysis

Projeto Integrador do curso de Engenharia da Computação para análise de dados de dengue utilizando dados abertos do Ministério da Saúde, com aplicação de técnicas de análise de dados e aprendizagem de máquina.

## 📌 Objetivo

Desenvolver uma aplicação capaz de coletar, tratar, analisar e visualizar dados de notificações de dengue, utilizando dados públicos disponibilizados pelo Ministério da Saúde.

O projeto também terá como objetivo explorar técnicas de aprendizagem de máquina para análise dos dados.

## 📊 Fonte dos dados

Os dados utilizados são provenientes da API de Dados Abertos do Ministério da Saúde.

**API utilizada:**

```text
https://apidadosabertos.saude.gov.br/arboviroses/dengue
```

A API disponibiliza notificações de dengue, permitindo consultas por ano e município.

### Parâmetros utilizados

* `nu_ano` — ano da ocorrência/notificação
* `id_municip` — código do município
* `limit` — quantidade de registros por página, com máximo de 1000
* `offset` — página dos resultados, iniciando em 0

## 🛠️ Tecnologias

Atualmente, o projeto utiliza:

* Python 3.14
* Requests
* Pandas
* NumPy
* Git/GitHub

Outras tecnologias serão adicionadas conforme o desenvolvimento do projeto.

## 📁 Estrutura atual

```text
dengue-analysis/

├── src/
│   └── api_test.py
├── .gitignore
├── README.md
├── requirements.txt
└── ...
```

## 💻 Pré-requisitos

Antes de iniciar o projeto, é necessário ter instalado:

* Python 3.14
* Git
* Acesso à internet

Para verificar a versão do Python instalada:

```powershell
python --version
```

Os comandos apresentados neste README consideram o uso do **Windows com PowerShell**.

## 🚀 Como iniciar o projeto

### 1. Clonar o repositório

No terminal:

```powershell
git clone URL_DO_REPOSITORIO
```

Depois, entre na pasta do projeto:

```powershell
cd dengue-analysis
```

> Substitua `URL_DO_REPOSITORIO` pela URL do repositório no GitHub.

### 2. Criar o ambiente virtual

Recomenda-se utilizar um ambiente virtual para instalar as dependências do projeto de forma isolada.

No Windows/PowerShell:

```powershell
python -m venv .venv
```

### 3. Ativar o ambiente virtual

No PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Após a ativação, o terminal deverá apresentar algo semelhante a:

```text
(.venv) PS C:\...\dengue-analysis>
```

### 4. Instalar as dependências

O arquivo `requirements.txt` contém as bibliotecas e versões utilizadas pelo projeto.

Com o ambiente virtual ativado:

```powershell
pip install -r requirements.txt
```

### 5. Executar o teste da API

Com o ambiente virtual ativado:

```powershell
python src/api_test.py
```

O programa realiza uma requisição à API do Ministério da Saúde e apresenta informações básicas sobre os dados recebidos.

Um resultado esperado é semelhante a:

```text
Status: 200
URL: https://apidadosabertos.saude.gov.br/arboviroses/dengue?nu_ano=2024&limit=10&offset=0

DataFrame:
...

Tipo dos dados: <class 'dict'>
Chaves: dict_keys(['dengue'])
Quantidade de registros: 10
```

> A quantidade e os dados apresentados podem variar conforme a disponibilidade e o comportamento da API.

## ⚠️ Observação sobre a API

O endereço utilizado atualmente pelo código é:

```text
https://apidadosabertos.saude.gov.br/arboviroses/dengue
```

**Não utilizar:**

```text
https://apidadosabertos.saude.gov.br/v1/arboviroses/dengue
```

O `/v1` aparece no endereço da documentação Swagger, porém o endpoint utilizado atualmente pelo projeto não contém `/v1`.

## 🌿 Fluxo de trabalho com Git

O projeto utiliza branches para permitir o desenvolvimento colaborativo.

Cada integrante deve trabalhar preferencialmente em uma branch própria, evitando realizar alterações diretamente na branch principal (`master`).

### Antes de iniciar uma nova tarefa

Primeiro, atualize a branch principal:

```powershell
git checkout master
git pull
```

Depois, crie uma branch para a tarefa:

```powershell
git checkout -b nome-da-tarefa
```

Exemplo:

```powershell
git checkout -b analise-dados
```

### Durante o desenvolvimento

Verifique as alterações realizadas:

```powershell
git status
```

Adicione os arquivos:

```powershell
git add .
```

Faça o commit:

```powershell
git commit -m "Descrição da alteração"
```

Envie a branch para o GitHub:

```powershell
git push -u origin nome-da-tarefa
```

Após o envio, a branch poderá ser revisada e integrada à branch principal.

## 👥 Desenvolvimento colaborativo

O fluxo recomendado para cada integrante é:

```text
master
  │
  ├── atualizar com git pull
  │
  └── criar branch da tarefa
          │
          ├── desenvolver
          ├── git status
          ├── git add
          ├── git commit
          └── git push
```

Ao iniciar uma nova tarefa, recomenda-se sempre partir da versão mais atualizada da branch `master`.

## 📌 Próximos passos

O projeto será desenvolvido de forma incremental. Entre as próximas etapas estão:

* [ ] Estudar o dicionário dos dados da API
* [ ] Definir as variáveis que serão utilizadas na análise
* [ ] Implementar a coleta de dados
* [ ] Implementar tratamento e limpeza dos dados
* [ ] Trabalhar com grandes volumes de registros e paginação da API
* [ ] Realizar análise exploratória dos dados
* [ ] Criar visualizações
* [ ] Definir e implementar modelo de aprendizagem de máquina
* [ ] Desenvolver uma interface para visualização dos resultados
* [ ] Implementar testes
* [ ] Avaliar utilização de banco de dados
* [ ] Avaliar utilização de serviços em nuvem

## 🎓 Projeto Integrador

Projeto desenvolvido como parte das atividades acadêmicas do curso de Engenharia da Computação.
