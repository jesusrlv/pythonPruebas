from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    fullname: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db = {
    "jesusrlv":{
        "username": "jesusrlv",
        "fullname": "rodolfo leaños",
        "email": "jesusrlv@hotmail.com",
        "disabled": False,
        "password": "123456789"
    },
    "jesusrlv2":{
        "username": "jesusrlv2",
        "fullname": "rodolfo leaños 2",
        "email": "jesusrlv2@hotmail.com",
        "disabled": True,
        "password": "987654321"
    }
}