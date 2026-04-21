from fastapi import APIRouter, HTTPException, Response, status, Depends
from sqlalchemy.orm import Session

router = APIRouter(
                    prefix = "/user",
                    tags = ['User']
                    )

@router.post("/")
def create_user():
    return {"data": "user_created"}

@router.get("/{user_id}")
def get_user(user_id:int):
    return {"data": user_id}
