from pydantic import BaseModel
from fastapi import APIRouter, status, HTTPException, Response, Depends
import services.user_services as services
from sqlalchemy.orm import Session

router = APIRouter()

class Post(BaseModel):
    title : str
    content : str
    published : bool = True

@router.get("/")
def get_posts(db: Session = Depends(services.get_db)):
    data = services.get_posts(db)
    return data

@router.post("/post", status_code= status.HTTP_201_CREATED)
def create_post(post:Post, db:Session = Depends(services.get_db)):
    try:
        return services.create_post(db, post)
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Something went wrong")

@router.get("/post/{id}", status_code=status.HTTP_200_OK)
def get_post(id: int, db:Session = Depends(services.get_db)):
    post = services.find_post(db, id)
    return {"data": post}

@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(services.get_db)):
    services.delete_post(db, id)
    return {Response(status_code = status.HTTP_204_NO_CONTENT)}

@router.put("/posts/{id}", status_code=status.HTTP_200_OK)
def update_post(id: int, post:Post, db: Session = Depends(services.get_db)):
    services.update(id, post, db)
    return  {"data":services.find_post(db, id)}
