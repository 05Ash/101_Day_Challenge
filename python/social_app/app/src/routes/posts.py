from fastapi import APIRouter, status, HTTPException, Response, Depends
from ..services.dependencies import get_db
from sqlalchemy.orm import Session

router = APIRouter(
                    prefix="/post",
                    tags=["Posts"]
                    )

@router.get("/s", status_code=status.HTTP_200_OK)
def get_all_posts(db: Session = Depends(get_db)):
    return {"data": "posts"}

@router.post("/", status_code = status.HTTP_201_CREATED)
def create_post():
    return {"data":"post created"}

@router.get("/{post_id}", status_code=status.HTTP_200_OK)
def get_post(post_id: int, db: Session = Depends(get_db)):
    return {"data": post_id}

@router.put("/{post_id}")
def update_post(post_id: int):
    return {"data": "post updated"}

@router.delete("/{post_id}")
def delete_post(post_id: int):
    return {"data": "post delted"}
