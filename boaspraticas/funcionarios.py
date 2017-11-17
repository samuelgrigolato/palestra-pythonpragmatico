"""Este módulo é responsável por trabalhar dados de funcionários"""

from itertools import groupby


class Funcionario(object): # pylint: disable=R0903
    """Representa um funcionário recuperado do Sistema de RH"""

    def __init__(self, cargo, salario):
        self.cargo = cargo
        self.salario = salario

    @property
    def remuneracao_por_hora(self):
        """Calcula a remuneração por hora de um funcionário,
        que é dada pela fórmula salario / 160"""
        return self.salario / 160


def custo_medio_por_tipo_servico(funcionarios, tipo_servico_do_cargo):
    """Retorna um dicionário onde a chave são tipos de serviço
    e o valor é uma tupla com a soma de custo desse tipo de serviço
    e o peso (quantidade de funcionários)"""

    # remove os funcionários que não possuem mapeamento de tipo de serviço
    funcionarios_validos = filter(lambda fun: fun.cargo in tipo_servico_do_cargo, funcionarios)

    funcionarios_por_tipo_servico = {
        tipo_servico: list(funs)
        for tipo_servico, funs in groupby(funcionarios_validos,
                                          lambda fun: tipo_servico_do_cargo[fun.cargo])
    }

    return {
        tipo_servico: (sum([fun.remuneracao_por_hora for fun in funs]), len(funs))
        for tipo_servico, funs in funcionarios_por_tipo_servico.items()
    }
