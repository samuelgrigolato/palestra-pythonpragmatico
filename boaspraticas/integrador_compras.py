"""Este módulo é responsável por integrar com o Sistema de Compras"""

import os
from json import load
from compras import Contrato


def carregar_contratos():
    """Chama o Sistema de Compras e busca todos os
    contratos existentes"""

    with open(os.path.dirname(__file__) + '/../compras/contratos.json') as arquivo:
        contratos = load(arquivo)

    return (
        Contrato(con['valor'], con['tipoDeServico'],
                 con['tipoDeContratacao'],
                 con['horasEstimadas'] if 'horasEstimadas' in con else None)
        for con in contratos
    )
