from pydantic import BaseModel
from fastapi import APIRouter, status, HTTPException, Response
import services.user_services as services


router = APIRouter()

class Post(BaseModel):
    title : str
    content : str
    published : bool = True

@router.get("/")
def get_posts():
    return services.get_posts()

@router.post("/posts", status_code= status.HTTP_201_CREATED)
def create_post(post:Post):
    try:
        services.create_post(post)
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Something went wrong")

@router.get("/posts/{id}", status_code=status.HTTP_200_OK)
def get_post(id: int):
    post = services.find_post(id)
    return {"data": post}

@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    services.delete_post(id)
    return Response(status_code = status.HTTP_204_NO_CONTENT)

@router.put("/posts/{id}", status_code=status.HTTP_200_OK)
def update_post(id: int, post:Post):
    services.update(id, post.model_dump())
    return  {"data":services.find_post(id)}
