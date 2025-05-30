
# mvp-full-stack-basico-front

Este é o Front-End do projeto MVP de arquitetura em microserviços, que apresenta uma interface web para operações de gerenciamento de estudantes. A aplicação permite autenticação de usuários via CPF e senha, cadastro e edição de estudantes, visualização de notas, além de funcionalidades de busca e deleção com suporte a rollback.

O objetivo deste projeto é demonstrar habilidades de integração entre um Front-End e um conjunto de APIs REST, simulando um cenário real de uma secretaria escolar automatizada, utilizando requisições HTTP para manipular dados de estudantes, usuários e notas.

---

## Estrutura do Projeto

### Arquivos Principais

1. **`index.html`**

   * Página de login do sistema.
   * Contém um formulário com campos de CPF e senha.
   * Redireciona o usuário autenticado com base no tipo (estudante, professor ou administrador).
2. **`school-secretary-student-grade.html`**

   * Tela principal da secretaria.
   * Permite visualizar, editar e deletar estudantes e suas notas.
   * Tabela dinâmica com inputs para cada nota e cálculo da média final.
3. **`school-secretary-student-sign-up.html`**

   * Página para cadastro de novos estudantes.
   * Formulário com campos de nome, CPF, série escolar, CEP e endereço.
   * Realiza integração com a API ViaCEP para preenchimento automático do endereço.
4. **`school-secretary-student-update.html`**

   * Tela de atualização de dados de estudantes existentes.
   * Busca por nome e formulário para edição de CEP e endereço.
5. **`scream_login.js`**

   * Script de autenticação de usuários.
   * Realiza validação de CPF, requisição de login, e redirecionamento baseado no tipo do usuário.
   * Armazena dados do usuário e notas no localStorage.
6. **`script.js`**

   * Contém a lógica principal de integração com os microserviços.
   * Funções de CRUD para estudantes, notas e usuários.
   * Validações de CPF, CEP e notas (0 a 10).
   * Lógica de rollback em caso de erro em operações críticas.
7. **`script_dropdown.js`**

   * Controla o menu lateral de navegação entre telas.
   * Adiciona acessibilidade e navegação por teclado e mouse.
   * Gerencia sessão e logout.
8. **`Dockerfile`**

   * Empacota a aplicação com NGINX para servir arquivos estáticos.
   * Expõe a porta 80 para acesso externo.

---

## Como Executar o Projeto

Este frontend é empacotado em uma imagem Docker com NGINX e exposto na porta 80.

1. Clone este repositório:

   ```
   git clone https://github.com/RafaelLambert/mvp-full-stack-basico-front.git
   cd mvp-full-stack-basico-front
   ```
2. Abra o terminal do projeto api-gateway e rode o git compose:

   ```
   docker-compose up --build

   ```
3. Verifique se os serviços estão online:

   ```
   docker ps
   ```
4. Teste a rota: *http://localhost:8080.*
5. Utilize a interface para realizar operações de CRUD nos estudantes.

### Pré-requisitos

* Navegador moderno (Google Chrome, Firefox, Edge, etc.).
* Docker instalado e funcional.
* APIs REST ativas nos seguintes endpoints:
  * Gateway
  * Student
  * Grade
  * Auth

## 🔌 Comunicação com os serviços

Este frontend consome as seguintes APIs:

| Serviço | Endpoint base                             | Porta Esperada |
| -------- | ----------------------------------------- | -------------- |
| Auth     | `http://localhost:5000/auth/user`       | 5000           |
| Student  | `http://localhost:5000/student/student` | 5000           |
| Grade    | `http://localhost:5000/grade/grade`     | 5000           |
| ViaCEP   | `https://viacep.com.br/ws/`             | Externa        |

## ✍️ Observações

- O login é baseado em CPF e tipo de usuário.
- O frontend armazena dados temporários no `localStorage` do navegador.
- Para que os usuários com permição de *admin/professor* possam acessar o sistema ele devem ser cadastrados manualmente utilizando diretamente o serviço de **auth**

## Requisitos funcionais a desenvolver

* Substituição de alerts por telas mais modernas e customizaveis.
* Adição de uma inteface para o estudante alterar sua senha.
* interface para cadastro de um usuário admin/professor.
* separação das interfaces entre admin/professor.

Este projeto é de uso acadêmico e segue as diretrizes da PUC-RIO para projetos de ensino.
