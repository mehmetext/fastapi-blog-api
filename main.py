from fastapi import FastAPI

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
