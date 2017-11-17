"""API principal"""

from flask import Flask, jsonify
import custo_medio

app = Flask(__name__) # pylint: disable=C0103


@app.route('/custo-por-tipo-servico')
def custo_por_tipo_servico():
    """Fornece custo médio por tipo de serviço"""
    return jsonify(custo_medio.agregar())
