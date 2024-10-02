### Autentificación 

from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from passlib.context import CryptContext

ALGORITHM = "HS256"

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl = "login")

crypt = CryptContext(schemes=["bcrypt"])

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
        "password": "$2a$12$EV2rIACOtIoMGDjaBcghW.FRmuqlTgVXJdN83Qc9kJQ2/Nt0MdlTC "
    },
    "jesusrlv2":{
        "username": "jesusrlv2",
        "fullname": "rodolfo leaños 2",
        "email": "jesusrlv2@hotmail.com",
        "disabled": True,
        "password": "$2a$12$5oiGDuO7DGwKthXc76x0E.Achq6xgaY.m/55hqXveJR5vVsEerpV. "
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST, detail="El usuario no existe")
    user = search_user_db(form.username)

    

    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")
    return {"access_token": user.username , "token_type": "bearer"}