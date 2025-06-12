from fastapi import APIRouter
from db.setup import db_dependency
import services.questionsServices as questionsServices
from db.schema import Questions as QuestionSchema
from typing import List

router = APIRouter()

@router.get("", response_model=List[QuestionSchema])
def get_questions(db: db_dependency):
    return questionsServices.getQuestions(db)
