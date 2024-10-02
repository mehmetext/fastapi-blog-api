from fastapi import FastAPI
from app.routers import hello

app = FastAPI(title="FastAPI Öğreniyorum")

app.include_router(hello.router)


""" @app.get("/")
async def root():
    return {"message": "Home Page!"}
 """
