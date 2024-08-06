from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#iniciar el server con: uvicorn users:app --reload

#entidad users
class User(BaseModel):
    id: int
    nombre: str
    surname: str
    url:str
    age: int

users_list = [
    User(id=1,nombre="Rodolfo",surname="jesusrlv",url="google.com",age=40),
    User(id=2,nombre="Jesus",surname="jesusrlv2",url="google.com.mx",age=42),
    User(id=3,nombre="JESUSrlv",surname="jesusrlv3",url="google.com.net",age=43),
    ]


@app.get("/usersjson")
async def usersjson():
    return [{
        "nombre":"Rodolfo",
        "surname":"jesusrlv",
        "url":"google.com",
        "age":40
            },
            {
        "nombre":"Jesus",
        "surname":"jesusrlv2",
        "url":"google.com.mx",
        "age":42
            },
            {
        "nombre":"JESUSrlv",
        "surname":"jesusrlv3",
        "url":"google.com.net",
        "age":43
            }
            ]

@app.get("/usersclass")
async def usersclass():
    return User(
        nombre="Rodolfo",
        surname="jesusrlv",
        url="google.com",
        age=40
        )

@app.get("/users")
async def users():
    return users_list

@app.get("/user/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
            return {"error":"no se ha encontrado el usuario"}

@app.get("/userquery/")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
            return {"error":"no se ha encontrado el usuario"}
