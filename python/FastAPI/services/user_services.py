from h11 import Response
from data.user_data import my_posts as posts
from fastapi import status, HTTPException

#Finds a post based on id
def find_post(id):
    index = find_index_post(id)
    return posts[index]

#Finds the index of a post
def find_index_post(id):
    for i, post in enumerate(posts):
        if post["id"] == id:
            return i
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post with id: {id} not found.")

def create_post(post):
    id = posts[-1]["id"] + 1
    my_post = post.model_dump()
    my_post["id"] = id
    posts.append(my_post)
    return {"data": "successfully published the post"}

def delete_post(id):
    index = find_index_post(id)
    posts.pop(index)

def update(id, post):
    index = find_index_post(id)
    post["id"] = id
    posts[index] = post
    return index
