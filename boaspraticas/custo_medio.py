"""Agregador de custos por tipo de serviço."""

from collections import defaultdict
from compras import custo_medio_por_tipo_servico as custo_medio_compras
from funcionarios import custo_medio_por_tipo_servico as custo_medio_funcionarios
import integrador_compras
import integrador_rh
import cargo_para_tipo_servico


def _incorporar_custos(agregador, custos):
    """Incorpora um dicionário de tipo_servico -> (valor, peso)
    em um dicionário de mesmo tipo, somando as parcelas de cada tupla"""
    for tipo_servico, custo in custos.items():
        existente = agregador[tipo_servico]
        agregador[tipo_servico] = (existente[0] + custo[0], existente[1] + custo[1])


def agregar():
    """Agrega custos de funcionários e compras"""

    contratos = integrador_compras.carregar_contratos()
    funcionarios = integrador_rh.carregar_funcionarios()
    mapeamento = cargo_para_tipo_servico.carregar()

    agregador = defaultdict(lambda: (0, 0))
    _incorporar_custos(agregador, custo_medio_compras(contratos))
    _incorporar_custos(agregador, custo_medio_funcionarios(funcionarios, mapeamento))

    return {
        tipo_servico: custo[0] / custo[1]
        for tipo_servico, custo
        in agregador.items()
    }
