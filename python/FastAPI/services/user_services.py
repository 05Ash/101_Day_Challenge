from fastapi import status, HTTPException
from settings import models
from services.server import SessionLocal, engine
from utilities import utils
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_user(user, db:Session):
    #hash the password
    user.password = utils.hash(user.password)
    try:
        user = models.Users(**user.model_dump())
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this email already exists."
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred."
        )

def find_user(id, db: Session):
    user = db.query(models.Users).filter(models.Users.id == id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = "User not found"
        )
    return user
