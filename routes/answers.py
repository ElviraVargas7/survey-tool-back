from fastapi import APIRouter
from db.setup import db_dependency
from db.schema import Answers as AnswerSchema
import services.answersServices as answersServices
import services.analyticsServices as analyticsServices
from typing import List

router = APIRouter()

@router.post("")
def submit_answers(answers: List[AnswerSchema], db: db_dependency):
    return answersServices.submitAnswers(answers, db)

@router.get("/averages")
def get_averages(db: db_dependency):
    return analyticsServices.getAverage(db)
