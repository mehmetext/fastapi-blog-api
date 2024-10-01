from datetime import datetime, time, timedelta
import random
from typing import List
import re
from uuid import UUID
from fastapi import Body, FastAPI, Path, Query
from enum import Enum
from pydantic import BaseModel, EmailStr, Field, HttpUrl

app = FastAPI()

""" 
@app.get("/")
async def root():
    return {"message": "Hello World from GET method"}


@app.post("/")
async def post():
    return {"message": "Hello World from POST method"}


@app.put("/{id}")
async def put():
    return {"message": "Hello World from PUT method"}


@app.delete("/{id}")
async def delete():
    return {"message": "Hello World from DELETE method"}


@app.get("/users")
async def list_users():
    return {"message": "List of users"}


@app.get("/users/me")
async def get_current_user():
    return {"message": "Current user"}


@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"message": f"user with id {user_id}"}


class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.fruits:
        return {"message": "Fruits are good for health"}
    if food_name == FoodEnum.vegetables:
        return {"message": "Vegetables are good for health"}
    if food_name == FoodEnum.dairy:
        return {"message": "Dairy products are good for health"}


fake_items = [
    {"item_name": "Tomato", "item_id": 1},
    {"item_name": "Potato", "item_id": 2},
    {"item_name": "Carrot", "item_id": 3},
    {"item_name": "Cabbage", "item_id": 4},
    {"item_name": "Cauliflower", "item_id": 5},
    {"item_name": "Cabbage", "item_id": 6},
    {"item_name": "Cauliflower", "item_id": 7},
    {"item_name": "Cabbage", "item_id": 8},
    {"item_name": "Cauliflower", "item_id": 9},
    {"item_name": "Cabbage", "item_id": 10},
    {"item_name": "Cauliflower", "item_id": 11},
    {"item_name": "Cabbage", "item_id": 12},
    {"item_name": "Cauliflower", "item_id": 13},
    {"item_name": "Cabbage", "item_id": 14},
    {"item_name": "Cauliflower", "item_id": 15},
    {"item_name": "Cabbage", "item_id": 16},
    {"item_name": "Cauliflower", "item_id": 17},
    {"item_name": "Cabbage", "item_id": 18},
    {"item_name": "Cauliflower", "item_id": 19},
]


@app.get("/items-old")
async def get_items(skip: int = 0, limit: int = 10):
    return fake_items[skip : skip + limit]


@app.get("/items-old/{item_id}")
async def get_item(item_id: int, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})

    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )

    return item


@app.get("/users/{user_id}/items/{item_id}")
async def get_user_item(
    user_id: int,
    item_id: int,
    sample_query: str,
    q: str | None = None,
    short: bool = False,
):
    item = {
        "item_id": item_id,
        "owner_id": user_id,
        "sample_query": sample_query,
    }
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/items")
async def create_item(item: Item):
    item_dict = item.model_dump()

    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})

    return item_dict


@app.put("/items/{item_id}")
async def create_item_with_put(item_id: int, item: Item):
    result = {"item_id": item_id, **item.model_dump()}
    return result


@app.get("/items")
async def read_items(
    q: str = Query(
        "asd",
        min_length=3,
        max_length=10,
    ),
    str_list: list[str] | None = Query(
        None,
        min_length=3,
        max_length=10,
        title="String List",
        description="Description for String List",
    ),
):
    results = {
        "items": [
            {"item_id": "Foo"},
            {"item_id": "Bar"},
        ],
        "q": q,
    }

    if str_list:
        results.update({"str_list": str_list})

    return results


@app.get("/items/hidden")
async def hidden_query_route(
    hidden_query: str | None = Query(None, include_in_schema=False),
):
    if hidden_query:
        return {"hidden_query": hidden_query}

    return {"hidden_query": "Not found"}


@app.get("/items_validation/{item_id}")
async def read_items_validation(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=10, le=100),
    q: str,
    size: float = Query(..., ge=0, le=10.5),
):
    results = {
        "item_id": item_id,
        "size": size,
        "random": random.randint(0, 100),
        "random_float": random.randint(0, 100) / 100,
    }

    if q:
        results.update({"q": q})

    return results
 """


""" class Item(BaseModel):
    name: str
    description: str = Field(..., min_length=10)
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., ge=0, le=150),
    q: str | None = None,
    item: Item | None = None,
    user: User | None = None,
    importance: int = Body(...),
):
    results = {
        "item_id": item_id,
        "q": q,
        "item": item,
        "user": user,
        "importance": importance,
    }

    return results
 """


""" class Image(BaseModel):
    url: HttpUrl = Field(..., example="https://example.com/foo.jpg")
    name: str = Field(..., example="A name")


class Item(BaseModel):
    name: str = Field(..., example="Foo")
    description: str | None = Field(None, example="A very nice item")
    price: float = Field(..., example=10.5)
    tax: float | None = Field(None, example=1.5)
    tags: List[str] | None = Field(None, example=["awesome", "nice"])
    images: List[Image] | None = Field(
        None,
        example=[
            {"url": "https://example.com/foo.jpg", "name": "A very nice item"},
        ],
    )


@app.put("/item/{item_id}")
async def update_item(item_id: int, item: Item = Body(embed=True)):
    results = {"item_id": item_id, **item.model_dump()}
    return results """


""" @app.put("/extra-data-types")
async def extra_data_types(
    item_id: UUID = Body(...),
    start_date: datetime = Body(...),
    end_date: datetime = Body(...),
    repeat_at: time = Body(...),
    process_after: timedelta = Body(...),
):
    duration = end_date - start_date
    print(duration)
    return {
        "item_id": item_id,
        "start_date": start_date,
        "end_date": end_date,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "duration": duration,
    }
 """


""" class User(BaseModel):
    id: UUID
    name: str
    age: int
    password: str
    email: EmailStr


@app.get(
    "/users",
    response_model=list[User],
)
async def get_users():
    users = [
        User(
            id=UUID("123e4567-e89b-12d3-a456-426614174000"),
            name="John Doe",
            age=25,
            password="123456",
            email="john.doe@example.com",
        ),
        User(
            id=UUID("123e4567-e89b-12d3-a456-426614174000"),
            name="John Doe",
            age=25,
            password="123456",
            email="john.doe@example.com",
        ),
    ]
    return users
 """


@app.post("/users", status_code=201)
async def create_item(name: str):
    return {"name": name}


@app.delete("/users/{id}", status_code=204)
async def delete_user(id: int):
    return {"id": id}


@app.get("/users/{id}", status_code=301)
async def read_user_redirect():
    return {"hello": "world"}
