# Entrega 3 - API SCHOOL SYSTEM + BANCO DE DADOS

## Integrantes:
Flávia Pereira

Luiz Nascimento Brito

Nicollas Gomes

Paula Entringer

---

## Objetivo

Apresentar as principais evoluções no projeto iniciado na Entrega 2, destacando a integração de banco de dados relacional com SQLAlchemy, documentação com Swagger, containerização com Docker, deploy na Render, controle de versões com GitHub (usando branches) e testes automatizados.

---

## 1. Introdução

### Objetivo Geral
A Entrega 2 tem como foco evoluir a aplicação previamente desenvolvida com Flask e arquitetura MVC, tornando-a mais robusta e preparada para ambientes reais de desenvolvimento e produção. A introdução de ferramentas modernas de deploy, documentação e automação foram priorizadas.

### Contexto
Dando continuidade ao projeto iniciado na Entrega 1, esta etapa incorporou elementos essenciais do ciclo de vida de aplicações modernas, como banco de dados, testes, deploy e documentação interativa. Essas mudanças refletem práticas exigidas no mercado, garantindo maior escalabilidade, manutenção e confiabilidade do sistema.

---

## 2. Descrição das Mudanças Implementadas

- Integração completa com SQLAlchemy e banco SQLite.  
- Documentação automática com Swagger (Flask-RESTX).  
- Dockerização da aplicação com Dockerfile e docker-compose.  
- Deploy na plataforma Render.  
- GitHub com branches separados por funcionalidades.  
- Implementação de testes com pytest.  

---

## 3. Procedimento de Implementação

### Etapas e Ferramentas Adotadas:

- **Modelos SQLAlchemy**  
  Criação de classes representando entidades da aplicação.

- **Controllers Atualizados**  
  Refatoração para incluir operações CRUD completas com persistência em banco.

- **Swagger (via Flask-RESTX)**  
  Criação de namespaces e rotas documentadas automaticamente, acessíveis via `/docs`.

- **Dockerização**  
  Dockerfile e docker-compose configurados.

- **Deploy na Render**  
  Projeto vinculado ao GitHub, com deploy automático a cada push.

- **Git e Branch Workflow**  
  - Branch develop: ambiente de integração.  
  - Branches de feature: isolam mudanças específicas.

- **Testes Automatizados**  
  Criação de testes unitários para cada entidade e integração com rotas.

---

## 4. Resultados Obtidos

- Rotas completas e persistência de dados funcionando.  
- Interface Swagger funcional.  
- Testes locais e remotos via Docker e Render.  
- Git colaborativo com controle de versões por branch.  
- Testes automatizados garantindo estabilidade.

---

## 5. Conclusão

A entrega consolidou o aprendizado em ORM, testes, deploy contínuo e boas práticas de versionamento. A aplicação evoluiu de um protótipo local para um sistema pronto para produção.
