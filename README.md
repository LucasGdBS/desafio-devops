# Desafio DevOps

## Descrição

O desafio consiste em criar uma pipeline de deploy automatizada para uma aplicação. A aplicação é uma API REST que realiza um CRUD de filmes. A aplicação foi desenvolvida em Python utilizando o framework FastAPI.

## Tecnologias utilizadas

| **Tecnologia** | **Versão** | **Descrição**                           |
|----------------|------------|-----------------------------------------|
| Python         | 3.12.7     | Linguagem de programação                |
| FastAPI        | 0.115.6    | Framework web para APIs REST            |
| SQLAlchemy     | 2.0.36     | ORM para mapeamento objeto-relacional   |
| Postgres       | 17         | Sistema de gerenciamento de banco de dados |
| Docker         |    | Plataforma para desenvolvimento, envio e execução de aplicativos |

## Execução local

Para executar a aplicação localmente com um banco de dados da sua escolha, siga os passos abaixo:

- Crie um arquivo `.env` na raiz do projeto seguindo o modelo do arquivo `.env.example` e preencha as variáveis de ambiente com os valores correspondentes.
- Troque a URL de conexão com o banco de dados no arquivo `.env` para a URL do seu banco de dados.
- Execute o comando `./runserver.sh` no bash para iniciar a aplicação. (O script irá criar um ambiente virtual, instalar as dependências do projeto e iniciar a aplicação)

Para executar a aplicação com o Docker, siga os passos abaixo:

- Execute o comando `docker-compose up` para iniciar a aplicação.

Depois basta acessar a URL `http://localhost:8000/docs` para visualizar a documentação da API e testar os endpoints.

## Github Actions

A pipeline de deploy foi criada utilizando o Github Actions. A pipeline é acionada a cada push na branch `main` e executa os seguintes passos:

- Puxa a versão mais recente da imagem do docker CLI e a usa como um contêiner base.
- Passa as credenciais do Railway e executa o comando railway up para fazer o deploy da aplicação.

A aplicaçao e o banco de dados são hospedados no Railway, um serviço de hospedagem de aplicativos que permite fazer o deploy de aplicativos de forma simples e rápida.

Pode ser acessado em: [https://desafio.up.railway.app/docs](https://desafio.up.railway.app/docs)
