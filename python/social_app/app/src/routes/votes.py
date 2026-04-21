from fastapi import APIRouter, status, HTTPException, Response, Depends
from sqlalchemy.orm import Session

router = APIRouter(
                    prefix = "/vote",
                    tags = ["Votes"]
                    )

@router.post("/")
def vote():
    return {"data": "voted"}
