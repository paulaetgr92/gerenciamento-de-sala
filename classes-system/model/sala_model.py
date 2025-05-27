import requests
from config import db

class Sala(db.Model):
    __tablename__ = 'salas'

    id = db.Column(db.Integer, primary_key=True)
    andar = db.Column(db.String(120), nullable=False)
    capacidade = db.Column(db.Integer, nullable=False)
    turma_id = db.Column(db.Integer, nullable=False)

    def __init__(self, andar, turma_id):
        self.andar = andar
        self.turma_id = turma_id
        self.capacidade = 0  

    def calcular_capacidade_com_base_na_turma(self):
        try:
            url = f"http://localhost:5003/alunos?turma_id={self.turma_id}"

            response = requests.get(url)

            if response.status_code == 200:
                alunos = response.json()
                self.capacidade = len(alunos) + 5
            else:
                raise Exception("Erro ao consultar alunos da turma")

        except Exception as e:
            raise Exception(f"Falha ao calcular capacidade: {str(e)}")

    def to_dict(self):
        return {
            'id': self.id,
            'andar': self.andar,
            'capacidade': self.capacidade,
            'turma_id': self.turma_id
        }


class SalaNaoEncontrada(Exception):
    def __init__(self, mensagem="Sala não encontrada"):
        super().__init__(mensagem)

def sala_por_id(id_sala):
    sala = Sala.query.get (id_sala)
    if not sala:
        return SalaNaoEncontrada (f'Sala não encontrada')
    return sala

def listar_sala():
    salas = Sala.query.all()
    return [sala.to_dict() for sala in salas]

def criar_sala(novos_dados):
    turma_id = novos_dados.get('turma_id')
    andar = novos_dados.get('andar')

    if not turma_id or not andar:
        return {"message": "Campos 'turma_id' e 'andar' são obrigatórios"}, 400

    sala_existente = Sala.query.filter_by(turma_id=turma_id).first()
    if sala_existente:
        return {"message": "Já existe uma sala para essa turma"}, 400

    nova_sala = Sala(andar=andar, turma_id=turma_id)

    try:
        nova_sala.calcular_capacidade_com_base_na_turma()  
        db.session.add(nova_sala)
        db.session.commit()

        return nova_sala.to_dict(), 201

    except Exception as e:
        db.session.rollback()
        return {"message": str(e)}, 500



def atualizar_sala(novos_dados, sala_id):
    sala = Sala.query.get(sala_id)

    if not sala:
        raise SalaNaoEncontrada(f"Sala com ID {sala_id} não encontrada")

    if 'andar' in novos_dados:
        sala.andar = novos_dados['andar']

    if 'turma_id' in novos_dados and novos_dados['turma_id'] != sala.turma_id:
        sala.turma_id = novos_dados['turma_id']
        try:
            sala.calcular_capacidade_com_base_na_turma()
        except Exception as e:
            return {"message": str(e)}, 500

    db.session.commit()
    return sala.to_dict(), 200


def excluir_sala(sala_id):
    sala = Sala.query.get(sala_id)

    if not sala:
        raise SalaNaoEncontrada(f"Sala com ID {sala_id} não encontrada")

    db.session.delete(sala)
    db.session.commit()

    return {"message": "Sala excluída com sucesso"}, 200
