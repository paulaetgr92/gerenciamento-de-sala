from flask import Blueprint, request, jsonify
from model.sala_model import (
    listar_sala,
    sala_por_id,
    criar_sala,
    atualizar_sala,
    excluir_sala,
    SalaNaoEncontrada
)

sala_bp = Blueprint('salas', __name__)

@sala_bp.route('/salas', methods=['GET'])
def endpoint_listar_salas():
    return jsonify(listar_sala()), 200


@sala_bp.route('/salas/<int:sala_id>', methods=['GET'])
def endpoint_sala_por_id(sala_id):
    try:
        sala = sala_por_id(sala_id)
        return jsonify(sala.to_dict()), 200
    except SalaNaoEncontrada as e:
        return jsonify({'message': str(e)}), 404


@sala_bp.route('/salas', methods=['POST'])
def endpoint_criar_sala():
    novos_dados = request.get_json()
    return criar_sala(novos_dados)

@sala_bp.route('/salas/<int:sala_id>', methods=['PUT'])
def endpoint_atualizar_sala(sala_id):
    novos_dados = request.get_json()
    try:
        return atualizar_sala(novos_dados, sala_id)
    except SalaNaoEncontrada as e:
        return jsonify({'message': str(e)}), 404

@sala_bp.route('/salas/<int:sala_id>', methods=['DELETE'])
def endpoint_excluir_sala(sala_id):
    try:
        return excluir_sala(sala_id)
    except SalaNaoEncontrada as e:
        return jsonify({'message': str(e)}), 404
