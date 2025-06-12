from sqlalchemy.orm import Session
from db.schema import Answers as AnswerSchema
import models
from typing import List

def submitAnswers(answers: List[AnswerSchema], db: Session):
    for answer in answers:
        dbAnswer = models.Answers(
            questionId=answer.questionId,
            rate=answer.rate
        )
        db.add(dbAnswer)
    
    db.commit()
    return {"message": f"{len(answers)} answers submitted successfully."}