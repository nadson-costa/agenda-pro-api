# Agenda Pro API

![CI/CD Pipeline](https://github.com/nadson-costa/agenda-pro-api/actions/workflows/deploy.yml/badge.svg)

API RESTful para um sistema de agendamento de horários, desenvolvida como um projeto de estudo aprofundado em Arquitetura e Engenharia de Software Back-End.

---

## Sobre o projeto

O "Agenda Pro" é o back-end de uma plataforma de agendamento pensada para profissionais de serviço (consultores, terapeutas, etc.). O objetivo do projeto foi construir uma aplicação do zero, seguindo as melhores práticas do mercado, para criar uma solução robusta, segura, testada e escalável.

## Principais funcionalidades

- **Gestão de usuários:** Cadastro de usuários com perfis de "cliente" e "profissional".
- **Autenticação segura:** Sistema de login com hashing de senhas (`bcrypt`) e autenticação via Tokens JWT.
- **Rotas protegidas:** Endpoints que só podem ser acessados por usuários autenticados e, em alguns casos, com perfis específicos.
- **Gestão de disponibilidade:** Endpoints para profissionais cadastrarem sua grade de horários de trabalho recorrente.
- **Consulta de horários:** Lógica complexa para calcular e retornar os horários livres de um profissional em uma data específica.
- **Criação de agendamentos:** Endpoint para clientes autenticados marcarem um horário com um profissional.

## Tecnologias e práticas que foram utilizadas

Este projeto foi construído com foco em demonstrar competências essenciais de um engenheiro de software profissional:

| Categoria | Tecnologias / Práticas |
| :--- | :--- |
| **Back-end** | Python, FastAPI, SQLAlchemy (ORM) |
| **Banco de dados** | PostgreSQL |
| **Testes** | Pytest, TestClient, Testes de Integração |
| **DevOps** | Docker, Docker Compose, CI/CD com GitHub Actions |
| **Segurança** | Hashing de Senhas (Passlib/Bcrypt), Tokens JWT |
| **Documentação** | Geração automática via FastAPI/Swagger (OpenAPI) |


## Como executar o projeto

Graças à containerização com Docker, o ambiente de desenvolvimento pode ser replicado com um único comando.

1. **Clone o repositório:**
    ```bash
    git clone [https://github.com/nadson-costa/agenda-pro-api.git](https://github.com/nadson-costa/agenda-pro-api.git)
    cd agenda-pro-api
    ```
2. **Crie o arquivo `.env`** a partir do exemplo `.env.example` (você precisará criar este arquivo de exemplo).

3. **Suba os contêineres:**
    ```bash
    docker compose up --build
    ```

4. A API estará disponível em `http://127.0.0.1:8000`.


## Documentação da API

A documentação interativa da API, gerada automaticamente pelo FastAPI, estará disponível, após você rodar o projeto, em:

- **Swagger UI:** [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs)
- **ReDoc:** [`http://127.0.0.1:8000/redoc`](http://127.0.0.1:8000/redoc)


## Backlog do projeto

Aprimoramentos futuros planejados:

- Expandir a cobertura de testes para incluir cenários de falha.
- Refinar o tratamento de erros com *exception handlers* globais.
- Introduzir um sistema de *migrations* de banco de dados com Alembic.
- Adicionar observabilidade básica com Prometheus e Grafana.
