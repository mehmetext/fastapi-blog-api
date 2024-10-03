from datetime import datetime
from pydantic import BaseModel, Field
from sqlalchemy import UUID, Column, DateTime, Integer, String, func
import uuid

from app.models import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid()
    )
    author_id = Column(Integer, nullable=False)

    title = Column(String, nullable=False)
    content = Column(String, nullable=False)

    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )


class PostBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=255)
    content: str = Field(..., min_length=3)
    author_id: int = Field(...)


class PostCreate(PostBase):
    pass


class PostUpdate(BaseModel):
    title: str | None = Field(None, min_length=3, max_length=255)
    content: str | None = Field(None, min_length=3)
    author_id: int | None = Field(None)


class PostRead(PostBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
