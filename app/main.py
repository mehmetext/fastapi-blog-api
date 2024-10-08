from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.lib import env
from app.models import Base
from app.routers import blog
from dotenv import load_dotenv
from app.lib import db

load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title=env.APP_NAME, lifespan=lifespan)

app.include_router(blog.router)
