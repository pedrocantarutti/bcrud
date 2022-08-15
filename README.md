# bcrud
Basic CRUD API written in Python3 with Flask and SQLite.

<hr>

## Usage

* API is running on a linode server.
- http://45.79.46.165:9000/v1
- Examples of requests and responses can be seen in Postman JSON file.

# Endpoint home

`GET /v1`
* Response: {"Message":"Basic CRUD API.","Result":true}

# Endpoint de usuários

### Listar todos usuários

`GET /v1/user/list`
* Response: 
![Screen Shot 2022-08-15 at 14 53 53](https://user-images.githubusercontent.com/4164887/184689015-6f350aff-dfde-4191-a17e-b018db3a14c7.png)


### Retornar um usuário especifico

`GET /v1/user/<id>`
* Request: /v1/user/6
* Response:
![Screen Shot 2022-08-15 at 14 53 14](https://user-images.githubusercontent.com/4164887/184688922-0f7b7603-2310-448f-891e-8af4b7bfa08d.png)


### Registrando novo usuário

`POST /v1/user`


### Atualizando usuário

`PUT /v1/user/<id>`


### Deletar usuário

`DELETE /v1/user/<id>`


### Autenticação do token com servidor JWT

`POST /v1/login`
