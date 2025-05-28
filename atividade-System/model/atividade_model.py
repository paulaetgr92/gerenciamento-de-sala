import requests
from config import db

class Atividade(db.Model):
    __tablename__ = 'atividades'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    enunciado = db.Column(db.Text, nullable=False)
    respostas = db.Column(db.Text)
    data_entrega = db.Column(db.String(20), nullable=False)
    professor_id = db.Column(db.Integer, nullable=False)

    def __init__(self, titulo, enunciado, respostas, data_entrega, professor_id):
        self.titulo = titulo
        self.enunciado = enunciado
        self.respostas = respostas
        self.data_entrega = data_entrega
        self.professor_id = professor_id
        self.validar_professor()

    def validar_professor(self):
        try:
            url = f"http://localhost:5003/professores/{self.professor_id}"
            response = requests.get(url)

            if response.status_code != 200:
                raise Exception(f"Professor com ID {self.professor_id} não encontrado")
        except Exception as e:
            raise Exception(f"Erro ao validar professor: {str(e)}")

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'enunciado': self.enunciado,
            'respostas': self.respostas,
            'data_entrega': self.data_entrega,
            'professor_id': self.professor_id
        }

    @staticmethod
    def listar_todos():
        return [a.to_dict() for a in Atividade.query.all()]

    @staticmethod
    def obter_por_id(id):
        atividade = Atividade.query.get(id)
        return atividade.to_dict() if atividade else None

    @staticmethod
    def criar(dados):
        nova = Atividade(
            titulo=dados['titulo'],
            enunciado=dados['enunciado'],
            respostas=dados.get('respostas', ''),
            data_entrega=dados['data_entrega'],
            professor_id=dados['professor_id']
        )
        db.session.add(nova)
        db.session.commit()
        return nova.to_dict()

    @staticmethod
    def atualizar(id, dados):
        atividade = Atividade.query.get(id)
        if not atividade:
            return None

        atividade.titulo = dados.get('titulo', atividade.titulo)
        atividade.enunciado = dados.get('enunciado', atividade.enunciado)
        atividade.respostas = dados.get('respostas', atividade.respostas)
        atividade.data_entrega = dados.get('data_entrega', atividade.data_entrega)
        atividade.professor_id = dados.get('professor_id', atividade.professor_id)

        # Revalidar professor se ID mudar
        atividade.validar_professor()

        db.session.commit()
        return atividade.to_dict()

    @staticmethod
    def deletar(id):
        atividade = Atividade.query.get(id)
        if not atividade:
            return False

        db.session.delete(atividade)
        db.session.commit()
        return True
