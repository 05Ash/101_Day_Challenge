from settings.config import UserCreate, UserResponse
from fastapi import APIRouter, status, Depends
from services import user_services as services
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/user/", status_code = status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(services.get_db)):
    return services.create_user(user, db)

@router.get("/user/{id}", status_code = status.HTTP_200_OK, response_model = UserResponse)
def get_user(id: int, db: Session = Depends(services.get_db)):
    return services.find_user(id, db)
