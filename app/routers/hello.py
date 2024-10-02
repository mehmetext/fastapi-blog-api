from fastapi import APIRouter

from app.models.hello import Hello

router = APIRouter(prefix="/hello", tags=["Hello"])


@router.get("/", response_model=Hello)
async def read_hello():
    return {"message": "Hello World"}
