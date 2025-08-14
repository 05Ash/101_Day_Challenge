from data.user_data import my_posts as posts

#Finds a post based on id
def find_post(id):
    for post in posts:
        if post["id"] == id:
            return post

#Finds the index of a post
def find_index_post(id):
    for i, post in enumerate(posts):
        if post["id"] == id:
            return i

def create_post(post):
    id = posts[-1]["id"] + 1
    my_post = post.model_dump()
    my_post["id"] = id
    posts.append(my_post)
    return {"data": "successfully published the post"}

def delete_post(index):
    posts.pop(index)
