# pylint: disable=C0103
# os nomes dos métodos podem ficar exagerados em suítes de teste
"""Suíte de testes unitários para o módulo funcionarios.py"""

from funcionarios import custo_medio_por_tipo_servico, Funcionario


def test_entradas_vazias():
    """Testa o cenário onde os parâmetros são listas vazias"""
    funcionarios = []
    tipo_servico_do_cargo = {}
    custos_medios = custo_medio_por_tipo_servico(funcionarios, tipo_servico_do_cargo)
    assert custos_medios == {}


def test_um_funcionario():
    """Testa o cenário onde um único funcionário é informado,
    sem nenhum mapeamento de cargo"""
    funcionarios = [
        Funcionario('Desenvolvedor Junior', 2000)
    ]
    tipo_servico_do_cargo = {}
    custos_medios = custo_medio_por_tipo_servico(funcionarios, tipo_servico_do_cargo)
    assert custos_medios == {}


def test_um_funcionario_com_mapeamento():
    """Testa o cenário onde um único funcionário é informado,
    com mapeamento de cargo correspondente"""
    funcionarios = [
        Funcionario('Desenvolvedor Junior', 1600)
    ]
    tipo_servico_do_cargo = {
        'Desenvolvedor Junior': 'DEV',
    }
    custos_medios = custo_medio_por_tipo_servico(funcionarios, tipo_servico_do_cargo)
    assert custos_medios == {
        'DEV': (10, 1)
    }


def test_viarios_funcionarios():
    """Testa o cenário onde vários funcionários são informados"""
    funcionarios = [
        Funcionario('Desenvolvedor Junior', 1600),
        Funcionario('Desenvolvedor Pleno', 3200),
        Funcionario('Barista', 16000),
        Funcionario('Desconhecido', 999),
    ]
    tipo_servico_do_cargo = {
        'Desenvolvedor Junior': 'DEV',
        'Desenvolvedor Pleno': 'DEV',
        'Barista': 'CAFE',
    }
    custos_medios = custo_medio_por_tipo_servico(funcionarios, tipo_servico_do_cargo)
    assert custos_medios == {
        'DEV': (30, 2),
        'CAFE': (100, 1),
    }
