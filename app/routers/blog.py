from fastapi import APIRouter
from app.controllers.blog import BlogController, OrderBy
from app.models.post import Post

router = APIRouter(prefix="/blog", tags=["Blog"])


@router.get("/", response_model=list[Post])
async def get_all_posts(
    q: str | None = None,
    author_id: int | None = None,
    order_by: OrderBy | None = None,
):
    return BlogController.get_all_posts(q, author_id, order_by)
