from fastapi import FastAPI
from app.lib import env
from app.routers import blog, hello_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title=env.APP_NAME)

app.include_router(hello_router.router)
app.include_router(blog.router)


""" @app.get("/")
async def root():
    return {"message": "Home Page!"}
 """
