from h11 import Response
from data.user_data import my_posts as posts
from fastapi import status, HTTPException
from services.server import cursor, connection

#Finds a post based on id
def get_posts():
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    print(posts)
    return posts

def find_post(id):
    cursor.execute(
        "SELECT * FROM posts WHERE post_id=%s",
        (id,)
    )
    post = cursor.fetchone()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post with id: {id} not found.")
    return post

#Finds the index of a post

def create_post(post):
    cursor.execute("INSERT INTO posts(title, content, published) VALUES(%s,%s,%s)",
                   (post.title, post.content, post.published)
    )
    connection.commit()

def delete_post(id):
    cursor.execute("DELETE FROM posts WHERE post_id=%s",
                   (id,))
    connection.commit()

def update(id, post):
    cursor.execute("""
                    UPDATE posts
                    SET
                        title=%s,
                        content=%s,
                        created_at=NOW()
                    WHERE post_id=%s\
                   """,
                   (post["title"], post["content"], id))
    connection.commit()
