from flask import Blueprint, request, jsonify
from model.horario_model import Horario, db, HorarioNaoEncontrado

horario_bp = Blueprint('horario_bp', __name__)

@horario_bp.route('/horarios', methods=['GET'])
def listar_horarios():
    horarios = Horario.query.all()
    return jsonify([h.to_dict() for h in horarios]), 200

@horario_bp.route('/horarios/<int:horario_id>', methods=['GET'])
def obter_horario(horario_id):
    horario = Horario.query.get(horario_id)
    if not horario:
        return jsonify({"message": "Horário não encontrado"}), 404
    return jsonify(horario.to_dict()), 200

@horario_bp.route('/horarios', methods=['POST'])
def criar_horario():
    dados = request.get_json()
    data = dados.get('data')
    hora_inicio = dados.get('hora_inicio')
    hora_fim = dados.get('hora_fim')
    sala_id = dados.get('sala_id')

    if not all([data, hora_inicio, hora_fim, sala_id]):
        return jsonify({"message": "Campos obrigatórios: data, hora_inicio, hora_fim, sala_id"}), 400

    novo_horario = Horario(data=data, hora_inicio=hora_inicio, hora_fim=hora_fim, sala_id=sala_id)
    try:
        db.session.add(novo_horario)
        db.session.commit()
        return jsonify(novo_horario.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500

@horario_bp.route('/horarios/<int:horario_id>', methods=['PUT'])
def atualizar_horario(horario_id):
    horario = Horario.query.get(horario_id)
    if not horario:
        return jsonify({"message": "Horário não encontrado"}), 404

    dados = request.get_json()
    horario.data = dados.get('data', horario.data)
    horario.hora_inicio = dados.get('hora_inicio', horario.hora_inicio)
    horario.hora_fim = dados.get('hora_fim', horario.hora_fim)
    horario.sala_id = dados.get('sala_id', horario.sala_id)

    try:
        db.session.commit()
        return jsonify(horario.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500

@horario_bp.route('/horarios/<int:horario_id>', methods=['DELETE'])
def excluir_horario(horario_id):
    horario = Horario.query.get(horario_id)
    if not horario:
        return jsonify({"message": "Horário não encontrado"}), 404

    try:
        db.session.delete(horario)
        db.session.commit()
        return jsonify({"message": "Horário excluído com sucesso"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500
