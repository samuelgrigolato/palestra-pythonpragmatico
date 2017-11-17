"""API principal"""

import xml.etree.ElementTree
import os
from json import load
from flask import Flask, jsonify
app = Flask(__name__) # pylint: disable=C0103


@app.route('/custo-por-tipo-servico')
def custo_por_tipo_servico():
    """Fornece custo médio por tipo de serviço"""

    with open(os.path.dirname(__file__) + '/../compras/contratos.json') as arquivo:
        contratos = load(arquivo)

    somas = dict()

    for contrato in contratos:

        tipo_servico = contrato['tipoDeServico']

        if tipo_servico not in somas:
            somas[tipo_servico] = (0, 0)

        soma_atual = somas[tipo_servico]
        valor_por_hora = (
            contrato["valor"] if contrato["tipoDeContratacao"] == 'H'
            else contrato["valor"] / contrato["horasEstimadas"]
        )
        somas[tipo_servico] = (soma_atual[0] + valor_por_hora, soma_atual[0] + 1)

    func_xml_path = os.path.dirname(__file__) + '/../rh/funcionarios.xml'
    raiz = xml.etree.ElementTree.parse(func_xml_path).getroot()
    for func in raiz:
        tipo_servico = 'DEV' # TODO aguardando solução do mapeamento de cargo para tipo de serviço
        salario = float(func.attrib['salario'])
        if tipo_servico not in somas:
            somas[tipo_servico] = (0, 0)

        soma_atual = somas[tipo_servico]
        somas[tipo_servico] = (soma_atual[0] + (salario / 168), soma_atual[0] + 1)

    medias = dict()

    for tipo_servico, soma in somas.items():
        medias[tipo_servico] = soma[0] / soma[1]

    return jsonify(medias)
