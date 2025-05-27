from config import db
from model.sala_model import Sala

class Horario(db.Model):  
    __tablename__ = 'horarios'

    id = db.Column(db.Integer, primary_key=True)  
    data = db.Column(db.String(20), nullable=False)
    hora_inicio = db.Column(db.String(10), nullable=False)
    hora_fim = db.Column(db.String(10), nullable=False)
    sala_id = db.Column(db.Integer, db.ForeignKey('salas.id'), nullable=False)  

    sala = db.relationship('Sala', backref='horarios', lazy=True)

    def __init__(self, data, hora_inicio, hora_fim, sala_id):
        self.data = data
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim
        self.sala_id = sala_id

    def to_dict(self):
        return {
            'id': self.id,
            'data': self.data,
            'hora_inicio': self.hora_inicio,
            'hora_fim': self.hora_fim,
            'sala_id': self.sala_id
        }


class HorarioNaoEncontrado(Exception):
    def __init__(self, mensagem="Horário não encontrado"):
        super().__init__(mensagem)


def reserva_por_horario_data(data, hora_inicio, sala_id):
    return Horario.query.filter_by(data=data, hora_inicio=hora_inicio, sala_id=sala_id).first()

def listar_datas():
    return [h.to_dict() for h in Horario.query.all()]

def criar_data(novos_dados):
    try:
        novo = Horario(
            data=novos_dados['data'],
            hora_inicio=novos_dados['hora_inicio'],
            hora_fim=novos_dados['hora_fim'],
            sala_id=novos_dados['sala_id']
        )
        db.session.add(novo)
        db.session.commit()
        return novo.to_dict(), 201
    except Exception as e:
        db.session.rollback()
        return {"message": str(e)}, 500

def atualizar_reserva_data(id, novos_dados):
    horario = Horario.query.get(id)
    if not horario:
        raise HorarioNaoEncontrado(f"Horário com ID {id} não encontrado")

    horario.data = novos_dados.get('data', horario.data)
    horario.hora_inicio = novos_dados.get('hora_inicio', horario.hora_inicio)
    horario.hora_fim = novos_dados.get('hora_fim', horario.hora_fim)
    horario.sala_id = novos_dados.get('sala_id', horario.sala_id)

    db.session.commit()
    return horario.to_dict(), 200

def excluir_reserva_data(id):
    horario = Horario.query.get(id)
    if not horario:
        raise HorarioNaoEncontrado(f"Horário com ID {id} não encontrado")

    db.session.delete(horario)
    db.session.commit()
    return {"message": "Reserva excluída com sucesso"}, 200
