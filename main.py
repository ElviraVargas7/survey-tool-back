from fastapi import FastAPI
import models
from db.setup import engine
from routes import members, answers, questions

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(members.router, prefix="/members", tags=["Members"])
app.include_router(answers.router, prefix="/answers", tags=["Answers"])
app.include_router(questions.router, prefix="/questions", tags=["Questions"])