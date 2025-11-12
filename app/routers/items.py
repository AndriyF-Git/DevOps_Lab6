from fastapi import APIRouter, HTTPException
from typing import List
from ..schemas import Item, ItemCreate

router = APIRouter()

ITEMS: List[Item] = []
NEXT_ID = 1


@router.get("/", response_model=List[Item])
def list_items():
    return ITEMS


@router.post("/", response_model=Item, status_code=201)
def create_item(payload: ItemCreate):
    global NEXT_ID
    item = Item(id=NEXT_ID, **payload.model_dump())
    NEXT_ID += 1
    ITEMS.append(item)
    return item


@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int):
    for it in ITEMS:
        if it.id == item_id:
            return it
    raise HTTPException(status_code=404, detail="Item not found")
