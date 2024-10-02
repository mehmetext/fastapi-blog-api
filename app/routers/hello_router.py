from fastapi import APIRouter

from app.controllers.hello_controller import HelloController
from app.models.hello_model import HelloModel

router = APIRouter(prefix="/hello", tags=["Hello"])


@router.get("/", response_model=HelloModel)
async def read_hello():
    return HelloController.read_hello()
