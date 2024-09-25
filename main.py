from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get(
    "/",
    tags=["Root"],
    responses={
        200: {
            "description": "Root",
            "content": {
                "application/json": {
                    "example": {"message": "Hello World from GET method"}
                }
            },
        }
    },
    status_code=200,
    deprecated=False,
)
async def root():
    return {"message": "Hello World from GET method"}


@app.post(
    "/",
    tags=["Root"],
    responses={
        200: {
            "description": "Root",
            "content": {
                "application/json": {
                    "example": {"message": "Hello World from POST method"}
                }
            },
        }
    },
    status_code=200,
    deprecated=False,
)
async def post():
    return {"message": "Hello World from POST method"}


@app.put(
    "/{id}",
    tags=["Root"],
    responses={
        200: {
            "description": "Root",
            "content": {
                "application/json": {
                    "example": {"message": "Hello World from PUT method"}
                }
            },
        }
    },
    status_code=200,
    deprecated=False,
)
async def put():
    return {"message": "Hello World from PUT method"}


@app.delete(
    "/{id}",
    tags=["Root"],
    responses={
        200: {
            "description": "Root",
            "content": {
                "application/json": {
                    "example": {"message": "Hello World from DELETE method"}
                }
            },
        }
    },
    status_code=200,
    deprecated=False,
)
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
