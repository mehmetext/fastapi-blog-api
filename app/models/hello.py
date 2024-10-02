from pydantic import BaseModel


class Hello(BaseModel):
    message: str
