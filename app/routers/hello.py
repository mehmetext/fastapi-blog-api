from fastapi import APIRouter

from app.models.hello import Hello


router = APIRouter(prefix="/hello")


@router.get("/", response_model=Hello)
async def read_hello():
    return {"message": "Hello World"}
