# 🎓 EduManage - Microservices Academic System

Este projeto é um MVP de um sistema acadêmico baseado em arquitetura de microserviços. Ele simula a gestão de estudantes, notas e autenticação de usuários, utilizando uma abordagem moderna, escalável e orientada a serviços. Todos os serviços são independentes e se comunicam via um API Gateway.

---

## 🔧 Tecnologias Utilizadas

- Python (Flask)
- Docker / Docker Compose
- REST APIs
- SQLite
- Flask-Cors, Requests, Pydantic
- JWT para autenticação
- Git / GitHub

---

## 🧱 Arquitetura
**Serviços:**
- **Auth Service**: Cadastro e login de usuários com JWT.
- **Student Service**: Gerenciamento de estudantes.
- **Grade Service**: Gerenciamento de notas.
- **Gateway**: Encaminha requisições para os serviços corretos.
- **Orchestrator**: Realiza operações complexas com rollback em caso de falha.
- **Frontend**: Interface web (opcional).

---

## ▶️ Como executar localmente

### Pré-requisitos

- Docker
- Docker Compose

### Passos:

```bash
# Clone o projeto
git clone https://github.com/seu-usuario/edu-microservices-mvp.git
cd edu-microservices-mvp

# Suba os containers
docker-compose up --build
