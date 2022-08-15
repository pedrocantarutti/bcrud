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
[
    {
        "cpf": "12332112356",
        "created_on": "Sun, 14 Aug 2022 13:24:35 GMT",
        "password": "3",
        "role": true,
        "updated_on": "Mon, 15 Aug 2022 02:01:05 GMT"
    },
]


### Retornar um usuário especifico

`GET /v1/user/<id>`
* Request: /v1/user/6
* Response:
{
    "cpf": "20",
    "create_on": "Mon, 15 Aug 2022 10:36:38 GMT",
    "password": "1",
    "role": false,
    "updated_on": "Mon, 15 Aug 2022 10:36:38 GMT"
}


### Registrando novo usuário

`POST /v1/user`


### Atualizando usuário

`PUT /v1/user/<id>`


### Deletar usuário

`DELETE /v1/user/<id>`


### Autenticação do token com servidor JWT

`POST /v1/login`
