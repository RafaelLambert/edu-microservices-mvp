# 🚪API Gateway - MVP Back-end - PUC-Rio

Este repositório contém o serviço de **API Gateway** do projeto MVP proposto pela PUC-Rio. O gateway foi desenvolvido utilizando Python com Flask e atua como ponto central para o encaminhamento de requisições HTTP entre os microsserviços da aplicação. Seu objetivo é simplificar a comunicação entre os serviços de forma segura, unificada e documentada.

O projeto está preparado para ser integrado com um front-end web, servindo como rota única para os microsserviços responsáveis por autenticação de usuários, gestão de estudantes e controle de notas.

---

## ⚙️Funcionalidades Principais

* **Roteamento Centralizado:** Todas as requisições para os serviços de estudante, notas e autenticação passam pelo gateway.
* **Proxy Transparente:** Encaminha chamadas HTTP (GET, POST, PUT, DELETE) com headers, corpo e query strings originais.
* **CORS Ativado:** Suporte a requisições de diferentes origens (cross-origin), facilitando a integração com aplicações front-end.
* **Preparado para Orquestração (Ainda não ativo):** Estrutura de rotas para integração futura com um serviço de orquestração, permitindo controle transacional em múltiplos microsserviços.

---

## 🛠️Tecnologias Utilizadas

* **Linguagem:** Python
* **Framework:** Flask
* **Documentação da API:** flask-openapi3
* **Controle de CORS:** Flask-CORS
* **Requisições HTTP:** requests
* **Containerização:** Docker + Docker Compose

---

## 🌐Endpoints da API

### 1. **Documentação**

* **Rota:** `/`
* **Método:** GET
* **Descrição:** Redireciona automaticamente para a interface Swagger da API.

---

### 2. **Encaminhamento para o Serviço de Estudantes**

* **Rota:** `/student/<path>`
* **Métodos:** GET, POST, PUT, DELETE
* **Descrição:** Encaminha chamadas para o microsserviço de estudantes.

---

### 3. **Encaminhamento para o Serviço de Notas**

* **Rota:** `/grade/<path>`
* **Métodos:** GET, POST, PUT, DELETE
* **Descrição:** Encaminha chamadas para o microsserviço de notas.

---

### 4. **Encaminhamento para o Serviço de Autenticação**

* **Rota:** `/auth/<path>`
* **Métodos:** GET, POST, PUT, DELETE
* **Descrição:** Encaminha chamadas para o microsserviço de autenticação.

---

### 5. *(A desenvolver – para futura orquestração)*

* **Rota:** `/gateway/register-student`
* **Método:** POST
* **Descrição:** Encaminha para o orquestrador registrar um estudante (ainda não implementado).
* **Rota:** `/gateway/delete-student`
* **Método:** DELETE
* **Descrição:** Encaminha para o orquestrador excluir um estudante (ainda não implementado).

---

## 🚀Como Executar o Projeto com Docker

### Pré-requisitos:

* Instalação do Docker
* instalação do WSL2

### Passos:

1. Clone este repositório e os repositórios dos outros microsserviços relacionados (caso ainda não tenha feito):

   ```bash
   git clone https://github.com/RafaelLambert/mvp-arquitetura-de-software-api-escola-front.git
   git clone https://github.com/RafaelLambert/mvp-arquitetura-de-software-api-gateway.git
   git clone https://github.com/RafaelLambert/mvp-arquitetura-de-software-api-auth.git
   git clone https://github.com/RafaelLambert/mvp-arquitetura-de-software-api-grade.git
   git clone https://github.com/RafaelLambert/mvp-arquitetura-de-software-api-student.git
   ```
2. Certifique-se de que o `docker-compose.yml` aponta corretamente para os diretórios dos serviços.
3. No diretório do gateway, execute:

   ```
    docker-compose up --build
   ```
4. A aplicação estará disponível em:

   * **Gateway:** [http://localhost:5000](http://localhost:5000)
   * **Front-end:** [http://localhost:8080](http://localhost:8080)
   * **Documentação Swagger:** [http://localhost:5000/openapi](http://localhost:5000/openapi)

---

## 📄Licença

Este projeto foi desenvolvido como parte de um MVP para a PUC-Rio e é destinado exclusivamente a fins educacionais.
