from datetime import UTC, datetime
import uuid
from pydantic import BaseModel
from sqlalchemy import UUID, Column, DateTime, Integer, String

from app.models import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    author_id = Column(Integer, nullable=False)

    title = Column(String, nullable=False)
    content = Column(String, nullable=False)

    created_at = Column(DateTime, nullable=False, default=datetime.now(UTC))
    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.now(UTC),
        onupdate=datetime.now(UTC),
    )


class PostBase(BaseModel):
    title: str
    content: str
    author_id: int


class PostCreate(PostBase):
    pass


class PostRead(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
