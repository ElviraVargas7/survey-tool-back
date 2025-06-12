from fastapi import FastAPI, Request
import models
from db.setup import engine, db_dependency
from sqlalchemy.orm import Session
import services.members as membersServices

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

@app.get("/members")
async def get_members(db: db_dependency):
    return membersServices.getMembers(db)