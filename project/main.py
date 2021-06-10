from enum import Enum
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


class Brand(str, Enum):
    nike = "nike"
    adidas = "adidas"


@app.get("/")
async def root():
    return {"message": "Hello Fast Api"}


# @app.get("/items/{item_id}")
# async def read_item(item_id:int):
#     return {"item_id": item_id}

@app.get("/brands/{brand_name}")
async def get_brand(brand_name: Brand):
    if brand_name == Brand.nike:
        return {"brand_name": brand_name, "message": "JUST DO IT."}

    if brand_name == Brand.adidas:
        return {"brand_name": brand_name, "message": "IMPOSSIBLE IS NOTHING."}


mock_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"}
]


@app.get("/items")
async def read_items(skip: int = 0, limit: int = 10):
    return mock_items_db[skip: skip + limit]


# @app.get("/items/{item_id}")
# async def get_item(item_id: str, q: Optional[str] = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}


@app.get("/items/{item_id}")
async def get_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "LOOOOOOONG Description."}
        )
    return item


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item