from pydantic import BaseModel


class HelloModel(BaseModel):
    message: str
