import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from fastapi import Depends
from typing import Annotated
from sqlalchemy.orm import Session

URL_DATABASE = config.DATABASE_URL
engine = create_engine(URL_DATABASE)

#configure the session to be used for db operations
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#serves as the base class fordeclarative models
Base = declarative_base()

#creates a db session using SessionLocal and yields it to the caller
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]