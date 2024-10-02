from fastapi import FastAPI
from app.routers import blog, hello

app = FastAPI(title="FastAPI Öğreniyorum")

app.include_router(hello.router)
app.include_router(blog.router)


""" @app.get("/")
async def root():
    return {"message": "Home Page!"}
 """
