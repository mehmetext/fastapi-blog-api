from enum import Enum
from fastapi import APIRouter
from app.models.post import Post
from app.data.posts import example_posts

router = APIRouter(prefix="/blog", tags=["Blog"])


class OrderBy(str, Enum):
    title = "title"
    content = "content"
    created_at = "created_at"
    updated_at = "updated_at"


@router.get("/", response_model=list[Post])
async def get_all_posts(
    q: str | None = None,
    author_id: int | None = None,
    order_by: OrderBy | None = None,
):
    posts = example_posts

    if q:
        print(f"q: {q}")
        posts = [
            post
            for post in posts
            if q.lower() in post.title.lower() or q.lower() in post.content.lower()
        ]
    if author_id:
        print(f"author_id: {author_id}")
        posts = [post for post in posts if post.author_id == author_id]

    print(f"Found posts count: {len(posts)}")

    if order_by:
        print(f"order_by: {order_by}")
        posts = sorted(posts, key=lambda x: getattr(x, order_by.value))

    return posts
