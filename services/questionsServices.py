from sqlalchemy.orm import Session
from typing import List
from db.schema import Questions as QuestionsSchema
import models

def getQuestions(db: Session) -> List[QuestionsSchema]:
    questions = db.query(models.Questions).all()
    return [QuestionsSchema(id=q.id, question=q.question) for q in questions]