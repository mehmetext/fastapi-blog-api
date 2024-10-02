from enum import Enum
from fastapi import HTTPException
from sqlalchemy import select
from app.models.post import Post, PostRead
from sqlalchemy.ext.asyncio import AsyncSession


class OrderBy(str, Enum):
    title_asc = "title_asc"
    title_desc = "title_desc"
    content_asc = "content_asc"
    content_desc = "content_desc"
    created_at_asc = "created_at_asc"
    created_at_desc = "created_at_desc"
    updated_at_asc = "updated_at_asc"
    updated_at_desc = "updated_at_desc"


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
            if order_by == OrderBy.title_asc:
                query = query.order_by(Post.title.asc())
            elif order_by == OrderBy.title_desc:
                query = query.order_by(Post.title.desc())
            elif order_by == OrderBy.content_asc:
                query = query.order_by(Post.content.asc())
            elif order_by == OrderBy.content_desc:
                query = query.order_by(Post.content.desc())
            elif order_by == OrderBy.created_at_asc:
                query = query.order_by(Post.created_at.asc())

        result = await db.execute(query)

        posts = result.scalars().all()

        print(f"Posts count: {len(posts)}")

        return posts

    async def get_post(db: AsyncSession, id: int) -> PostRead:
        result = await db.execute(select(Post).where(Post.id == id))
        post = result.scalar()

        if not post:
            raise HTTPException(status_code=404, detail="Post not found")

        return post
