from enum import Enum
import uuid
from fastapi import HTTPException
from sqlalchemy import select
from app.lib.utils import random_word
from app.models.post import Post, PostCreate, PostRead, PostUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from slugify import slugify


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
            elif order_by == OrderBy.created_at_desc:
                query = query.order_by(Post.created_at.desc())
            elif order_by == OrderBy.updated_at_asc:
                query = query.order_by(Post.updated_at.asc())
            elif order_by == OrderBy.updated_at_desc:
                query = query.order_by(Post.updated_at.desc())

        result = await db.execute(query)

        posts = result.scalars().all()

        print(f"Posts count: {len(posts)}")

        return posts

    async def get_post(db: AsyncSession, id: uuid.UUID) -> PostRead:
        result = await db.execute(select(Post).where(Post.id == id))
        post = result.scalar()

        if not post:
            raise HTTPException(status_code=404, detail="Post not found")

        return post

    async def create_post(db: AsyncSession, post: PostCreate) -> PostRead:
        slug = slugify(post.title)

        existing_post = await db.execute(select(Post).where(Post.slug == slug))

        if existing_post:
            slug = f"{slug}-{random_word(5)}"

        new_post = Post(**post.model_dump(), slug=slug)

        db.add(new_post)
        await db.commit()
        await db.refresh(new_post)

        return new_post

    async def update_post(
        db: AsyncSession,
        id: uuid.UUID,
        post: PostUpdate,
    ) -> PostRead:
        result = await db.execute(select(Post).where(Post.id == id))
        existing_post = result.scalar()

        if not existing_post:
            raise HTTPException(status_code=404, detail="Post not found")

        for key, value in post.model_dump(exclude_unset=True).items():
            setattr(existing_post, key, value)

        slug = slugify(existing_post.title)

        existing_slug_check = await db.execute(select(Post).where(Post.slug == slug))

        if existing_slug_check:
            slug = f"{slug}-{random_word(5)}"

        existing_post.slug = slug

        await db.commit()
        await db.refresh(existing_post)

        return existing_post

    async def delete_post(db: AsyncSession, id: uuid.UUID) -> None:
        result = await db.execute(select(Post).where(Post.id == id))
        post = result.scalar()

        if not post:
            raise HTTPException(status_code=404, detail="Post not found")

        await db.delete(post)
        await db.commit()
