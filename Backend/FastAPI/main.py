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

#para echar a andar el server de prueba es #source .venv/bin/activate
#y para desactivar el server es deactivate

# cargar el server de fastAPI uvicorn users:app --reload 