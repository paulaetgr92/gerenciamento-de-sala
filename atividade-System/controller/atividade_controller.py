from flask import Blueprint, request, jsonify
from model.atividade_model import Atividade

atividade_bp = Blueprint('atividade_bp', __name__, url_prefix='/atividades')

# Listar todas as atividades
@atividade_bp.route('/', methods=['GET'])
def listar():
    return jsonify(Atividade.listar_todos()), 200

# Obter atividade por ID
@atividade_bp.route('/<int:id>', methods=['GET'])
def obter(id):
    atividade = Atividade.obter_por_id(id)
    if not atividade:
        return jsonify({'message': 'Atividade não encontrada'}), 404
    return jsonify(atividade), 200

# Criar nova atividade
@atividade_bp.route('/', methods=['POST'])
def criar():
    dados = request.get_json()
    try:
        nova = Atividade.criar(dados)
        return jsonify(nova), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Atualizar atividade
@atividade_bp.route('/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.get_json()
    try:
        atualizada = Atividade.atualizar(id, dados)
        if not atualizada:
            return jsonify({'message': 'Atividade não encontrada'}), 404
        return jsonify(atualizada), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Deletar atividade
@atividade_bp.route('/<int:id>', methods=['DELETE'])
def deletar(id):
    if Atividade.deletar(id):
        return jsonify({'message': 'Atividade removida com sucesso'}), 200
    return jsonify({'message': 'Atividade não encontrada'}), 404
