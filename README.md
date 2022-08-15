# bcrud
Basic CRUD API written in Python3 with Flask and SQLite.

<hr>

## Usage

* API is running on a linode server.
- http://45.79.46.165:9000/v1

# Endpoint de usuários

### Listar todos usuários

`GET /v1/users`


### Retornar um usuário especifico

`GET /v1/user/<id>`


### Registrando novo usuário

`POST /v1/user`


### Atualizando usuário

`PUT /v1/user/<id>`


### Deletar usuário

`DELETE /v1/user/<id>`


### Autenticação do token com servidor JWT

`POST /v1/login`
