

## Integrantes:
Flávia Pereira

Luiz Nascimento Brito

Nicollas Gomes

Paula Entringer

---


## Data da Realização da Atividade
28/05/2025

---

## 1. Introdução

### Objetivo Geral
Apresentar uma nova funcionalidade implementada no projeto: a API de Turmas, com integração a banco de dados relacional, documentação via Swagger, deploy, testes automatizados e containerização com Docker.

### Contexto
Expandindo o escopo do sistema de gestão escolar iniciado anteriormente, foi desenvolvida uma API para gerenciar turmas, com vinculação direta a `sala_id`, seguindo boas práticas de arquitetura MVC e uso de ORM com SQLAlchemy.

---

## 2. Descrição das Mudanças Implementadas

- Criação da API `Gerenciamento de salas` com rotas CRUD completas.  
- Relacionamento com a entidade `turma_id` via chave estrangeira.  
- Integração com SQLAlchemy.  
- Documentação com Swagger (Flask-RESTX).  
- Dockerização da aplicação.  
- Deploy na Render via GitHub.  
- Controle de versão com Git (workflow com branches).  
- Testes automatizados com pytest.

---

## 3. Procedimento de Implementação

### Modelo SQLAlchemy:
```python
class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sala_id = db.Column(db.Integer, db.ForeignKey('sala.id'), nullable=False)
```

### Endpoints:
```python
@turma_bp.route('/turmas', methods=['GET']) def listar_turmas(): ...
@turma_bp.route('/turmas/<int:turma_id>', methods=['GET']) def turma_por_id(turma_id): ...
@turma_bp.route('/turmas', methods=['POST']) def criar_turma(): ...
@turma_bp.route('/turmas/<int:turma_id>', methods=['PUT']) def atualizar_turma(turma_id): ...
@turma_bp.route('/turmas/<int:turma_id>', methods=['DELETE']) def excluir_turma(turma_id): ...
```

### Outros Itens:
- Documentação acessível em `/docs`.  
- Dockerfile e docker-compose configurados.   

---

## 4. Resultados Obtidos

- API de turmas funcionando com operações CRUD.  
- Associação correta com salas existentes.  
- Testes cobrindo funcionalidades principais.

---

