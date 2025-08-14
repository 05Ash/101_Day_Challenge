from typing import Optional
from pydantic import BaseModel
from fastapi import APIRouter, status, HTTPException
import services.user_services as services
from data.user_data import my_posts as posts

router = APIRouter()

class Post(BaseModel):
    title : str
    content : str
    publish : bool = True
    rating : Optional[int] = None

@router.get("/")
def get_posts():
    return posts

@router.post("/posts", status_code= status.HTTP_201_CREATED)
def create_post(post:Post):
    try:
        services.create_post(post)
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Something went wrong")

@router.get("/posts/{id}", status_code=status.HTTP_200_OK)
def get_post(id: int):
    post = services.find_post(id)
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Post with id: {id} not found")
    return {"data": post}

@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    print(1)
    index = services.find_index_post(id)
    print(index)
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Post with id: {id} not found")
    services.delete_post(index)
    return {"data":"Post successfully delted"}
