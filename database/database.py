from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from fastapi import Depends
from typing import Annotated
from database.database import engine, SessionLocal
from sqlalchemy.orm import Session

URL_DATABASE = 'postgresql://postgres:test123!@localhost:5432/survey'
engine = create_engine(URL_DATABASE)

#configure the session to be used for db operations
Sessionlocal = sessionmaker(auocommit=False, autoflush=False, bind=engine)

#serves as the base class fordeclarative models
Base = declarative_base()

#creates a db session using SessionLocal and yields it to the caller
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.Close()

db_dependency = Annotated[Session, Depends(get_db)]