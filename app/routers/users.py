from fastapi import APIRouter, HTTPException
from typing import Dict
from ..schemas import User

router = APIRouter()

USERS: Dict[int, User] = {
    1: User(id=1, name="Alice"),
    2: User(id=2, name="Bob"),
}

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    user = USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user