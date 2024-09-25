from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

app = FastAPI()


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


@app.get("/items")
async def get_items(skip: int = 0, limit: int = 10):
    return fake_items[skip : skip + limit]


@app.get("/items/{item_id}")
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
