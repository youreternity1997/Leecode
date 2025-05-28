from typing import Annotated
from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# 掛載 static 目錄，讓 /login.html 能直接被存取
app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.post("/login/")
async def login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
):
    return {"username": username}

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="127.0.0.1", port=8000)