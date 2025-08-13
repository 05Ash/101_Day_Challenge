# Import FastAPI
import enum
from typing import Optional
from fastapi import FastAPI, Response,status, HTTPException
from pydantic import BaseModel


# Create app instance
app = FastAPI()

#Authenicating the post data
class Post(BaseModel):
    title: str
    content: str
    publish: bool = True
    rating: Optional[int] = None

my_posts = [{"title":"title of post1", "content": "content of post 1", "id":1}, {"title": "favoirite foods", "content": "I like pizza", "id": 2}]

#Finds a post based on id
def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post

#Finds the index of a post
def find_index_post(id):
    for i, post in enumerate(my_posts):
        if post["id"] == id:
            return i

# Define a route using the @app.get decorator
@app.get("/")
def read_root():
    return {"Data": my_posts}

@app.post("/posts", status_code = status.HTTP_201_CREATED)
def create_posts(post : Post):
    new_post = post.model_dump()
    new_post["id"] = new_post.get("id",my_posts[-1]["id"]) + 1
    my_posts.append(new_post)

    return {"Data" : "Successfully published the post"}

@app.get("/posts/{id}")
def get_post(id : int, response : Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"post with id: {id} was not found")

    return {"post_detail": post}


@app.delete("/posts/{id}", status_code = status.HTTP_202_ACCEPTED)

def delete_post(id : int):
    index = find_index_post(id)
    print(index)
    if index:
        my_posts.pop(index)
    return {"message": "post successfully deleted"}
