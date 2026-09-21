# Dicionário de dados - Projeto Integrador IV
# Análise de dados de Dengue
#
# As descrições devem ser conferidas com o dicionário
# oficial disponibilizado pelo Ministério da Saúde.

DICIONARIO_DADOS = {
    "tp_not": {
        "descricao": "Tipo de notificação",
        "tipo": "categórica"
    },

    "id_agravo": {
        "descricao": "Código do agravo",
        "tipo": "categórica"
    },

    "dt_notific": {
        "descricao": "Data da notificação",
        "tipo": "data"
    },

    "nu_ano": {
        "descricao": "Ano da notificação",
        "tipo": "numérica"
    },

    "sg_uf_not": {
        "descricao": "Unidade Federativa da notificação",
        "tipo": "categórica"
    },

    "id_municip": {
        "descricao": "Código do município",
        "tipo": "categórica"
    },

    "cs_sexo": {
    "descricao": "Sexo",
    "tipo": "categórica",
    "codigos": {
        "F": "Feminino",
        "M": "Masculino"
    }
},

    "cs_gestant": {
        "descricao": "Situação de gestação",
        "tipo": "categórica"
    },

    "cs_raca": {
        "descricao": "Raça/cor",
        "tipo": "categórica"
    },

    "cs_escol_n": {
        "descricao": "Escolaridade",
        "tipo": "categórica"
    },

    "sg_uf": {
        "descricao": "Unidade Federativa de residência",
        "tipo": "categórica"
    },

    "ano_nasc": {
        "descricao": "Ano de nascimento",
        "tipo": "numérica"
    },

    "febre": {
        "descricao": "Presença de febre",
        "tipo": "categórica"
    },

    "mialgia": {
        "descricao": "Presença de mialgia",
        "tipo": "categórica"
    },

    "cefaleia": {
        "descricao": "Presença de cefaleia",
        "tipo": "categórica"
    },

    "exantema": {
        "descricao": "Presença de exantema",
        "tipo": "categórica"
    },

    "vomito": {
        "descricao": "Presença de vômito",
        "tipo": "categórica"
    },

    "nausea": {
        "descricao": "Presença de náusea",
        "tipo": "categórica"
    },

    "diarreia": {
        "descricao": "Presença de diarreia",
        "tipo": "categórica"
    },

    "artralgia": {
        "descricao": "Presença de artralgia",
        "tipo": "categórica"
    },

    "diabetes": {
        "descricao": "Registro de diabetes",
        "tipo": "categórica"
    },

    "hipertensa": {
        "descricao": "Registro de hipertensão",
        "tipo": "categórica"
    },

    "hospitaliz": {
        "descricao": "Registro de hospitalização",
        "tipo": "categórica"
    },

    "classi_fin": {
        "descricao": "Classificação final do caso",
        "tipo": "categórica"
    },

    "criterio": {
        "descricao": "Critério de confirmação do caso",
        "tipo": "categórica"
    },

    "tpautocto": {
        "descricao": "Classificação quanto à origem do caso",
        "tipo": "categórica"
    },

    "evolucao": {
        "descricao": "Evolução do caso",
        "tipo": "categórica"
    },

    "dt_obito": {
        "descricao": "Data do óbito",
        "tipo": "data"
    },

    "dt_encerra": {
        "descricao": "Data de encerramento",
        "tipo": "data"
    },

    "dt_pcr": {
        "descricao": "Data da realização do exame PCR",
        "tipo": "data"
    },

    "resul_pcr_": {
        "descricao": "Resultado do exame PCR",
        "tipo": "categórica"
    },

    "sorotipo": {
        "descricao": "Sorotipo identificado",
        "tipo": "categórica"
    }
}


def mostrar_dicionario():
    """Exibe as variáveis cadastradas no dicionário."""

    for variavel, informacoes in DICIONARIO_DADOS.items():

        print(
            f"{variavel}: "
            f"{informacoes['descricao']} "
            f"({informacoes['tipo']})"
        )

        if "codigos" in informacoes:
            print("  Códigos:")

            for codigo, significado in informacoes["codigos"].items():
                print(f"    {codigo} = {significado}")

if __name__ == "__main__":
    mostrar_dicionario()