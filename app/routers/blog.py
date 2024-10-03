import uuid
from fastapi import APIRouter, Depends, Path, Query
from app.controllers.blog import BlogController, OrderBy
from app.lib.db import get_db
from app.models.post import PostRead
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/blog", tags=["Blog"])


@router.get(
    "/",
    response_model=list[PostRead],
    summary="Get all blog posts",
    description="Retrieve a list of all blog posts with optional filtering and sorting",
)
async def get_all_posts(
    q: str | None = Query(
        None,
        min_length=3,
        description="Search query for posts",
    ),
    author_id: int | None = Query(
        None,
        description="Filter posts by author ID",
    ),
    order_by: OrderBy | None = Query(
        None,
        description="Order posts by a specific field",
        example="created_at_asc",
    ),
    db: AsyncSession = Depends(get_db),
):
    return await BlogController.get_all_posts(db, q, author_id, order_by)


@router.get(
    "/{id}",
    response_model=PostRead,
    summary="Get a single blog post by ID",
    description="Retrieve a single blog post by its unique identifier",
)
async def get_post(
    id: uuid.UUID = Path(
        ...,
        description="The ID of the post to retrieve",
        example="123e4567-e89b-12d3-a456-426614174000",
    ),
    db: AsyncSession = Depends(get_db),
):
    return await BlogController.get_post(db, id)
