from enum import Enum
from fastapi import FastAPI

app = FastAPI()

class Brand(str, Enum):
    nike = "nike"
    adidas = "adidas"

@app.get("/")
async def root():
    return {"message": "Hello Fast Api"}

@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id": item_id}

@app.get("/brands/{brand_name}")
async def get_brand(brand_name: Brand):
    if brand_name == Brand.nike:
        return {"brand_name": brand_name, "message": "JUST DO IT."}

    if brand_name == Brand.adidas:
        return {"brand_name": brand_name, "message": "IMPOSSIBLE IS NOTHING."}
