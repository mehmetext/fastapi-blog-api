from fastapi import APIRouter

from app.models.post import Post

router = APIRouter(prefix="/blog", tags=["Blog"])


@router.get("/", response_model=list[Post])
async def get_all_posts(q: str | None = None, author_id: int | None = None):
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

    return posts


example_posts = [
    Post(
        id=1,
        title="Introduction to FastAPI",
        content="FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.",
        author_id=1,
        created_at="2024-01-15T09:30:00Z",
        updated_at="2024-01-15T09:30:00Z",
    ),
    Post(
        id=2,
        title="Python Best Practices",
        content="Explore the best practices for writing clean, efficient, and maintainable Python code.",
        author_id=2,
        created_at="2024-01-20T14:45:00Z",
        updated_at="2024-01-21T10:15:00Z",
    ),
    Post(
        id=3,
        title="RESTful API Design",
        content="Learn the principles of designing robust and scalable RESTful APIs for your web applications.",
        author_id=1,
        created_at="2024-02-05T11:00:00Z",
        updated_at="2024-02-06T16:30:00Z",
    ),
    Post(
        id=4,
        title="Asynchronous Programming in Python",
        content="Dive into asynchronous programming concepts and their implementation in Python using asyncio.",
        author_id=3,
        created_at="2024-02-10T08:20:00Z",
        updated_at="2024-02-10T08:20:00Z",
    ),
    Post(
        id=5,
        title="Database Integration with SQLAlchemy",
        content="Explore how to integrate SQLAlchemy with FastAPI for efficient database operations in your web applications.",
        author_id=2,
        created_at="2024-02-18T13:40:00Z",
        updated_at="2024-02-19T09:10:00Z",
    ),
]
