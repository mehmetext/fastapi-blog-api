from enum import Enum
from sqlalchemy import select
from app.lib.data.posts import example_posts
from app.models.post import Post, PostRead
from sqlalchemy.ext.asyncio import AsyncSession


class OrderBy(str, Enum):
    title = "title"
    content = "content"
    created_at = "created_at"
    updated_at = "updated_at"


class BlogController:
    async def get_all_posts(
        db: AsyncSession,
        q: str | None = None,
        author_id: int | None = None,
        order_by: OrderBy | None = None,
    ) -> list[PostRead]:
        query = select(Post)

        if q:
            print(f"q: {q}")
            query = query.where(
                Post.title.ilike(f"%{q}%") | Post.content.ilike(f"%{q}%")
            )

        if author_id:
            print(f"author_id: {author_id}")
            query = query.where(Post.author_id == author_id)

        if order_by:
            print(f"order_by: {order_by}")
            query = query.order_by(getattr(Post, order_by.value))

        result = await db.execute(query)

        posts = result.scalars().all()

        print(f"Posts count: {len(posts)}")

        return posts

    async def get_post(id: int) -> PostRead:
        post = next((post for post in example_posts if post.id == id), None)
        return post
