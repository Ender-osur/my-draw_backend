from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Esta api es dedicada a la perroncha de la Rubena Carrascal"}
