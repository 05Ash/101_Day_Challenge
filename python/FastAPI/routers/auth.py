from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from services.server import get_db
from settings.config import UserLogin
from services import auth_services as services
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(
                    tags = ['Authentication']
                    )

@router.post("/login", status_code = status.HTTP_200_OK)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    token = services.user_login(user_credentials, db)
    return token
