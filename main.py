from fastapi import FastAPI
import models
from db.setup import engine
from routes import members, answers, questions
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # This is the next.js frontend ✨
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(members.router, prefix="/members", tags=["Members"])
app.include_router(answers.router, prefix="/answers", tags=["Answers"])
app.include_router(questions.router, prefix="/questions", tags=["Questions"])
