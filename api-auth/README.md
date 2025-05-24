
# 🔐API Auth - MVP Back-end - PUC-Rio

Este repositório contém o microsserviço de **gestão de usuários** do projeto MVP proposto pela PUC-Rio. O serviço foi desenvolvido em Python utilizando o framework Flask, com SQLAlchemy para a modelagem do banco de dados e Pydantic para validação de dados.

Ele fornece uma API REST documentada com Swagger para cadastro, autenticação, listagem, atualização e exclusão de usuários.

---

## ⚙️Funcionalidades Principais

* **Cadastro de Usuários:** Registra novos usuários com CPF, senha e tipo (ex: aluno, professor).
* **Autenticação:** Verifica CPF e senha do usuário (login).
* **Listagem de Usuários:** Retorna todos os usuários cadastrados.
* **Consulta por CPF:** Permite buscar um usuário pelo CPF.
* **Atualização de Senha:** Atualiza a senha de um usuário.
* **Remoção de Usuários:** Remove um usuário com base no CPF.

---

## 🛠️Tecnologias Utilizadas

* **Linguagem:** Python
* **Framework Web:** Flask
* **Validação:** Pydantic
* **ORM:** SQLAlchemy
* **Extensões:** Flask-CORS, flask-openapi3
* **Documentação:** Swagger (via flask-openapi3)
* **Banco de Dados:** SQLite (padrão), com suporte a outros via SQLAlchemy
* **Testes:** nose2
* **Tipagem:** typing_extensions

---

## 🌐Endpoints da API

### 📄 Documentação

* **Rota:** `/`
* **Método:** GET
* **Descrição:** Redireciona para a interface de documentação Swagger/OpenAPI.

---

### ➕ Cadastro de Usuário

* **Rota:** `/user`
* **Método:** POST
* **Descrição:** Adiciona um novo usuário.
* **Body Exemplo:**

```json
{
  "cpf": "12345678900",
  "password": "Senha123",
  "user_type": "student"
}
```

---

### 📋 Listagem de Usuários

* **Rota:** `/users`
* **Método:** GET
* **Descrição:** Lista todos os usuários cadastrados.

---

### 🔍 Busca por CPF (GET)

* **Rota:** `/user`
* **Método:** GET
* **Query Param:** `cpf=12345678900`
* **Descrição:** Retorna os dados do usuário com base no CPF.

---

### 🔎 Busca por CPF (POST)

* **Rota:** `/user/search`
* **Método:** POST
* **Descrição:** Retorna os dados do usuário com base no CPF (forma segura).
* **Body Exemplo:**

```json
{
  "cpf": "12345678900"
}
```

---

### 🔐 Login

* **Rota:** `/user/login`
* **Método:** POST
* **Descrição:** Autentica o usuário com CPF e senha.
* **Body Exemplo:**

```json
{
  "cpf": "12345678900",
  "password": "Senha123"
}
```

---

### ✏️ Atualização de Senha

* **Rota:** `/user`
* **Método:** PUT
* **Query Param:** `cpf=12345678900`
* **Body Exemplo:**

```json
{
  "password": "NovaSenha456"
}
```

---

### 🗑️ Remoção de Usuário

* **Rota:** `/user`
* **Método:** DELETE
* **Query Param:** `cpf=12345678900`
* **Descrição:** Remove o usuário com o CPF informado.

---

## 🚀Como Executar o Projeto

### Executando Localmente com Virtual Enviroment

#### Pré-requisitos:

* Python 3.10+
* pip (gerenciador de pacotes)
* (Opcional) Ambiente virtual

#### Passos:

1. Clone este repositório:

```bash
git clone https://github.com/RafaelLambert/mvp-arquitetura-de-software-api-auth.git
cd mvp-arquitetura-de-software-api-auth
```

2. Crie e ative o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute a aplicação:

```bash
python app.py
```

A aplicação estará disponível em: [http://localhost:5003](http://localhost:5003)
A documentação Swagger estará disponível em: [http://localhost:5003/openapi](http://localhost:5003/openapi)

---

### 🐳Executando via Dockerfile

#### Pré-requisitos:

* Docker
* Docker Compose
* WSL2 (para usuários Windows)

#### Passos:

1. Clone este repositório:

```bash
git clone https://github.com/RafaelLambert/mvp-arquitetura-de-software-api-auth.git
cd mvp-arquitetura-de-software-api-auth
```

2. Acesse o terminal e entre na distro padrão (caso WSL):

```bash
wsl
```

3. Construa a imagem Docker:

```bash
docker build -t api-auth .
```

4. Verifique se a imagem foi criada:

```bash
docker images
```

5. Rode o container:

```bash
docker run -d -p 5003:5003 --name container-auth api-auth
```

6. Verifique os containers ativos:

```bash
docker ps
```

7. A aplicação estará disponível em:

* **API Auth:** [http://localhost:5003](http://localhost:5003)
* **Documentação Swagger:** [http://localhost:5003/openapi](http://localhost:5003/openapi)

---

### 🐳 Executando com Docker Compose

#### Pré-requisitos:

* Docker
* Docker Compose (no serviço de Gateway)
* WSL2 (para usuários Windows)

#### Passos:

1. Clone este e os demais repositórios que compõem o sistema de microserviços:

```bash
git clone https://github.com/RafaelLambert/mvp-arquitetura-de-software-api-escola-front.git
git clone https://github.com/RafaelLambert/mvp-arquitetura-de-software-api-gateway.git
git clone https://github.com/RafaelLambert/mvp-arquitetura-de-software-api-auth.git
git clone https://github.com/RafaelLambert/mvp-arquitetura-de-software-api-grade.git
git clone https://github.com/RafaelLambert/mvp-arquitetura-de-software-api-student.git
```

2. Certifique-se de que o `docker-compose.yml` está no diretório do *gateway*.
3. Execute o seguinte comando no diretório do gateway:

```bash
docker-compose up --build
```

4. A aplicação estará disponível em:

* **API Auth:** [http://localhost:5003](http://localhost:5003)
* **Documentação Swagger:** [http://localhost:5003/openapi](http://localhost:5003/openapi)

---

## 📄Licença

Este projeto foi desenvolvido como parte de um MVP para a PUC-Rio e é destinado exclusivamente a fins educacionais.
