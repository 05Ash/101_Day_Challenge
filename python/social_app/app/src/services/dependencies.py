from fastapi import FastAPI, APIRouter, Depends, HTTPException, Response, status
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from ..settings.config import settings as set

DATABASE_URL = f'postgresql://{set.database_username}:{set.database_password}@{set.database_address}:{set.database_port}/{set.database}'

Base = declarative_base()

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind = engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
