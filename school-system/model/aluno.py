from datetime import date, datetime
import sys
import os

# Garante que o diretório base esteja no caminho para importações
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import db
from model.turma import Turma

class Aluno(db.Model):
    __tablename__ = 'alunos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    nota_primeiro_semestre = db.Column(db.Float, nullable=False)
    nota_segundo_semestre = db.Column(db.Float, nullable=False)
    media_final = db.Column(db.Float, nullable=False)

    turma_id = db.Column(db.Integer, db.ForeignKey("turmas.id"), nullable=False)
    turma = db.relationship('Turma', backref='alunos', lazy=True)

    def __init__(self, nome, idade, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre, turma_id):
        self.nome = nome
        self.idade = idade
        self.data_nascimento = data_nascimento
        self.nota_primeiro_semestre = nota_primeiro_semestre
        self.nota_segundo_semestre = nota_segundo_semestre
        self.turma_id = turma_id
        self.media_final = self.calcular_media_final()

    def calcular_idade(self):
        hoje = date.today()
        return hoje.year - self.data_nascimento.year - ((hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day))

    def calcular_media_final(self):
        return (self.nota_primeiro_semestre + self.nota_segundo_semestre) / 2

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'data_nascimento': self.data_nascimento.isoformat(),
            'nota_primeiro_semestre': self.nota_primeiro_semestre,
            'nota_segundo_semestre': self.nota_segundo_semestre,
            'media_final': self.media_final,
            'turma_id': self.turma_id
        }

# Exceção personalizada
class AlunoNaoEncontrado(Exception):
    pass

# CRUD Functions

def aluno_por_id(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado(f'Aluno não encontrado')
    return aluno

def listar_alunos():
    alunos = Aluno.query.all()
    return [aluno.to_dict() for aluno in alunos]

def adicionar_aluno(novos_dados):
    turma = db.session.get(Turma, novos_dados['turma_id'])
    if turma is None:
        return {"message": "Turma não existe"}, 404

    data_nascimento = datetime.strptime(novos_dados['data_nascimento'], "%Y-%m-%d").date()
    idade = calcular_idade_from_data(data_nascimento)

    novo_aluno = Aluno(
        nome=novos_dados['nome'],
        idade=idade,
        data_nascimento=data_nascimento,
        nota_primeiro_semestre=float(novos_dados['nota_primeiro_semestre']),
        nota_segundo_semestre=float(novos_dados['nota_segundo_semestre']),
        turma_id=int(novos_dados['turma_id'])
    )

    db.session.add(novo_aluno)
    db.session.commit()
    return {"message": "Aluno adicionado com sucesso!"}, 201

def atualizar_aluno(id_aluno, novos_dados):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado("Aluno não encontrado")

    aluno.nome = novos_dados['nome']
    aluno.data_nascimento = datetime.strptime(novos_dados['data_nascimento'], "%Y-%m-%d").date()
    aluno.idade = calcular_idade_from_data(aluno.data_nascimento)
    aluno.nota_primeiro_semestre = float(novos_dados['nota_primeiro_semestre'])
    aluno.nota_segundo_semestre = float(novos_dados['nota_segundo_semestre'])
    aluno.media_final = aluno.calcular_media_final()
    aluno.turma_id = int(novos_dados['turma_id'])

    db.session.commit()

def excluir_aluno(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado(f'Aluno não encontrado.')

    db.session.delete(aluno)
    db.session.commit()

# Função utilitária
def calcular_idade_from_data(data_nasc):
    hoje = date.today()
    return hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
