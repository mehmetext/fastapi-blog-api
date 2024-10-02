from datetime import datetime
from pydantic import BaseModel


class Post(BaseModel):
    id: int
    title: str
    content: str
    author_id: int
    created_at: datetime
    updated_at: datetime
