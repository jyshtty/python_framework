import asyncio
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(title="Async CRUD API", version="1.0.0")

# In-memory storage with async lock for safe concurrent access
items: dict[int, dict] = {}
next_id = 1
lock = asyncio.Lock()


class ItemCreate(BaseModel):
    name: str = Field(min_length=5, max_length=10)
    description: Optional[str] = None
    price: float


class ItemUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=5, max_length=10)
    description: Optional[str] = None
    price: Optional[float] = None


class ItemResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float


@app.post("/items", response_model=ItemResponse, status_code=201)
async def create_item(item: ItemCreate):
    global next_id
    async with lock:
        items[next_id] = item.model_dump()
        created = ItemResponse(id=next_id, **items[next_id])
        next_id += 1
    return created


@app.put("/items/{item_id}", response_model=ItemResponse)
async def update_item(item_id: int, item: ItemUpdate):
    async with lock:
        if item_id not in items:
            raise HTTPException(status_code=404, detail="Item not found")
        updates = {k: v for k, v in item.model_dump().items() if v is not None}
        items[item_id].update(updates)
        return ItemResponse(id=item_id, **items[item_id])


@app.get("/items", response_model=list[ItemResponse])
async def list_items():
    async with lock:
        return [ItemResponse(id=k, **v) for k, v in items.items()]


@app.get("/items/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int):
    async with lock:
        if item_id not in items:
            raise HTTPException(status_code=404, detail="Item not found")
        return ItemResponse(id=item_id, **items[item_id])


@app.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: int):
    async with lock:
        if item_id not in items:
            raise HTTPException(status_code=404, detail="Item not found")
        del items[item_id]
