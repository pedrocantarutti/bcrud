# bcrud
Basic CRUD API written in Python3 with Flask and SQLite.

<hr>

## Usage

* API is running on a linode server.
- http://45.79.46.165:9000/v1
- Examples of requests and responses can be seen in Postman JSON file.

# Endpoint home

`GET /v1`
* Response: 

```json
{
  "Message": "Basic CRUD API.",
  "Result": true
}
```

# Endpoint de usuários

### Listar todos usuários

`GET /v1/user/list`
* Response: 
```json
[
    {
        "cpf": "12332112334",
        "created_on": "Sun, 14 Aug 2022 13:24:35 GMT",
        "password": "3",
        "role": true,
        "updated_on": "Mon, 15 Aug 2022 02:01:05 GMT"
    }
]
```

### Retornar um usuário especifico

`GET /v1/user/<id>`
* Request: /v1/user/1
* Response:
```json
{
    "cpf": "20",
    "create_on": "Mon, 15 Aug 2022 16:52:54 GMT",
    "password": "1",
    "role": false,
    "updated_on": "Mon, 15 Aug 2022 16:52:54 GMT"
}
```

### Registrando novo usuário

`POST /v1/user`
* Request: /v1/user
  * Body:
  ```json
  {
    "cpf":"200",
    "password": "1",
    "role": true
  } 
  ```
* Response: "User 200 create on 2022-08-15 16:52:54.195903"

### Atualizando usuário

`PUT /v1/user/<id>`
* Request: /v1/user/1
  * Param: token
  * Body:
   ```json
   
   ```
* Response:
```json

```

### Deletar usuário

`DELETE /v1/user/<id>`
* Request: /v1/user/1
  * Param: token 
* Response:
```json

```

### Autenticação do token com servidor JWT

`POST /v1/login`
* Request: /v1/login
  * params: token   
* Response:
```json
{
    "Message": "User 1 is logged in.",
    "Result": true,
    "expiration_date": "Mon, 15 Aug 2022 18:07:31 GMT",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjcGYiOiIyMCIsImV4cCI6MTY2MDU4Njg1MX0.M_dQqap0hT4LzX0AFWcZRTNVsG6MOD2KGmk4IP5AGRY"
}
```
