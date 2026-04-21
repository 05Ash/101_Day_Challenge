from fastapi import APIRouter, HTTPException, status, Depends, Response
from sqlalchemy.orm import Session

router = APIRouter(
                    prefix = "/comment",
                    tags = ["Comments"]
                    )

@router.get("s/{post_id}")
def get_comments_by_post(post_id: int):
    return {"data": post_id}

@router.get("s/{user_id}")
def get_comments_by_user(user_id: int):
    return {"data": user_id}

@router.post("/create")
def create_comment():
    return {"data": "comment created"}

@router
