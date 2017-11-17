"""Este módulo fornece um mapeamento de cargos para
tipos de serviço"""

import os


def carregar():
    """Retorna um dicionário onde a chave é o cargo
    e o valor é o tipo de serviço correspondente"""

    with open(os.path.dirname(__file__) + '/../rh/cargo_para_tipo_servico.csv') as arquivo:
        tuplas = [linha.split(',') for linha in arquivo]

    return {
        tupla[0]: tupla[1][:-1] # o [:-1] retira a quebra de linha no final
        for tupla in tuplas
    }
