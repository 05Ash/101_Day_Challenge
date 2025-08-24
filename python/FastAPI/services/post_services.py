from fastapi import status, HTTPException
from settings import models
from services.server import engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

# #Finds a post based on id
def get_posts(db: Session):
    posts = db.query(models.Post).all()
    return posts

def find_post(db: Session, post_id):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post with id: {post_id} not found.")
    return post

def create_post(db: Session, post):
    try:
        new_post = models.Post(**post.model_dump())
        db.add(new_post)
        db.commit()
        # No returning possible with alchemy, so use refresh to put the value back to new_post
        db.refresh(new_post)
        return new_post
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred"
        )

def delete_post(db:Session, id):
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post with id: {id} not found.")
    post.delete(synchronize_session = False)
    db.commit()

def update(id, post, db: Session):
    updated_post = db.query(models.Post).filter(models.Post.id == id)
    if updated_post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post with id: {id} not found.")
    updated_post.update(post.model_dump(), synchronize_session = False)
    db.commit()
