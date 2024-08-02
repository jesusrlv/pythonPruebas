from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "hola mundo fastAPI"

@app.get("/url")
async def root():
    return {"url_curso":"http://google.com",
            "nombre":"jesus",
            "apellido":"leaños",
            "nickname":"jesusrlv"
            }

#para echar a andar el server de prueba de fastAPI es 