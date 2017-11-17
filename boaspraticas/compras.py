"""Este módulo é responsável por trabalhar dados de compras"""

from itertools import groupby


class Contrato(object): # pylint: disable=R0903
    """Representa um contrato recuperado do Sistema de Compras"""

    def __init__(self, valor, tipo_servico, tipo_contratacao, horas_estimadas=None):
        self.valor = valor
        self.tipo_servico = tipo_servico
        self.tipo_contratacao = tipo_contratacao
        self.horas_estimadas = horas_estimadas

    @property
    def valor_por_hora(self):
        """Calcula o valor hora de um contrato,
        que pode ser o próprio valor para contratos
        pagos por hora ou o valor dividido pelas
        horas estimadas em contratos de escopo fechado"""
        if self.tipo_contratacao == 'H':
            return self.valor
        elif self.tipo_contratacao == 'E':
            return self.valor / self.horas_estimadas
        else:
            raise Exception('Tipo de contratação desconhecido! ' + self.tipo_contratacao)


def custo_medio_por_tipo_servico(contratos):
    """Retorna um dicionário onde a chave são tipos de serviço
    e o valor é uma tupla com a soma dos custos desse tipo de serviço
    e o peso (quantidade de ocorrências) dos contratos feitos pela empresa"""
    contratos_por_tipo_servico = {
        tipo_servico: list(cons)
        for tipo_servico, cons
        in groupby(contratos, lambda con: con.tipo_servico)
    }
    return {
        tipo_servico: (sum(con.valor_por_hora for con in cons), len(cons))
        for tipo_servico, cons in contratos_por_tipo_servico.items()
    }
