# pylint: disable=C0103
# os nomes dos métodos podem ficar exagerados em suítes de teste
"""Suíte de testes unitários para o módulo compras.py"""

from compras import custo_medio_por_tipo_servico, Contrato


def test_entradas_vazias():
    """Testa o cenário onde o parâmetro é uma lista vazia"""
    contratos = []
    custos_medios = custo_medio_por_tipo_servico(contratos)
    assert custos_medios == {}


def test_um_contrato():
    """Testa o cenário onde um único contrato é informado"""
    contratos = [
        Contrato(125, 'DEV', 'H')
    ]
    custos_medios = custo_medio_por_tipo_servico(contratos)
    assert custos_medios == {
        'DEV': (125, 1)
    }


def test_varios_contratos():
    """Testa o cenário onde vários contratos são informados"""
    contratos = [
        Contrato(125, 'DEV', 'H'),
        Contrato(15000, 'DEV', 'E', horas_estimadas=100),
        Contrato(100, 'CAFE', 'H')
    ]
    custos_medios = custo_medio_por_tipo_servico(contratos)
    assert custos_medios == {
        'DEV': (275, 2),
        'CAFE': (100, 1),
    }
