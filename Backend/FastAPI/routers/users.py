from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

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


@router.get("/usersjson")
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

@router.get("/usersclass")
async def usersclass():
    return User(
        nombre="Rodolfo",
        surname="jesusrlv",
        url="google.com",
        age=40
        )

@router.get("/users")
async def users():
    return users_list

#path
@router.get("/user/{id}")
async def user(id: int):
    return search_user(id)
    # users = filter(lambda user: user.id == id, users_list)
    # try:
    #     return list(users)[0]
    # except:
    #         return {"error":"no se ha encontrado el usuario"}


#query
@router.get("/user/")
async def user(id: int):
    # users = filter(lambda user: user.id == id, users_list)
    return search_user(id)
    # try:
    #     return list(users)[0]
    # except:
    #         return {"error":"no se ha encontrado el usuario"}

def search_user(id:int):
     users = filter(lambda user: user.id == id, users_list)
     try:
        return list(users)[0]
     except:
         return {"error":"el usuario ya existe"}
     
@router.post("/user/",status_code=201)
async def user(user: User): #se trae los datos de User con los tipados
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
        #return {"error":"no se ha encontrado el usuario"}
    else:

        users_list.append(user)
        return user

@router.put("/user/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error":"no se ha actualizado el usuario"}
    else:
        return user
    
@router.delete("/user/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"error":"no se ha eliminado el usuario"}