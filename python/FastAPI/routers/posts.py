from settings.config import PostCreate, PostResponse
from fastapi import APIRouter, status, HTTPException, Response, Depends
from services import post_services as services
from services.server import get_db
from sqlalchemy.orm import Session
from typing import List
from tokens import oauth2

router = APIRouter(
                    prefix="/post",
                    tags=['Posts']
                    )

@router.get("/home", status_code=status.HTTP_200_OK)
def root():
    return {"message": "Welcome"}

@router.get("s/", status_code=status.HTTP_200_OK, response_model = List[PostResponse])
def get_posts(db: Session = Depends(get_db)):
    data = services.get_posts(db)
    return data

@router.post("/", status_code= status.HTTP_201_CREATED, response_model = PostResponse)
def create_post(post:PostCreate, db:Session = Depends(get_db), user_id:int = Depends(oauth2.get_current_user)):
    try:
        print(user_id)
        return services.create_post(db, post)
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Something went wrong")

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model= PostResponse)
def get_post(id: int, db:Session = Depends(get_db)):
    post = services.find_post(db, id)
    return post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    services.delete_post(db, id)
    return {Response(status_code = status.HTTP_204_NO_CONTENT)}

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=PostResponse)
def update_post(id: int, post:PostCreate, db: Session = Depends(get_db)):
    services.update(id, post, db)
    return  services.find_post(db, id)
