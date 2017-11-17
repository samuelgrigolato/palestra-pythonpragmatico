"""Este módulo é responsável por integrar com o Sistema de RH"""

import os
import xml.etree.ElementTree
from funcionarios import Funcionario


def carregar_funcionarios():
    """Chama o Sistema de RH e busca todos os
    funcionários da empresa"""

    arquivo_xml = os.path.dirname(__file__) + '/../rh/funcionarios.xml'
    raiz = xml.etree.ElementTree.parse(arquivo_xml).getroot()

    return (
        Funcionario(fun.attrib['cargo'], float(fun.attrib['salario']))
        for fun in raiz
    )
