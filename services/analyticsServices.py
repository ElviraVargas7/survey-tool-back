import models
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Dict

def getAverage(db: Session) -> List[Dict]:
    results = (
    db.query(
        models.Questions.id,
        models.Questions.question,
        func.avg(models.Answers.rate).label("average_rate"),
        func.count(models.Answers.id).label("responses")
    )
    .join(models.Answers, models.Questions.id == models.Answers.questionId)
    .group_by(models.Questions.id, models.Questions.question)
    .all()
    )

    return [
        {
            "questionId": r.id,
            "question": r.question,
            "average_rate": round(r.average_rate, 2),
            "responses": r.responses
        }
        for r in results
    ]