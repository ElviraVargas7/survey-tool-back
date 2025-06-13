from fastapi import APIRouter
from db.setup import db_dependency
from db.schema import Answers as AnswerSchema
from typing import List
from fastapi.responses import StreamingResponse
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import services.answersServices as answersServices
import services.membersServices as memberServices
import services.analyticsServices as analyticsServices
from services.reportGenerator import generate_survey_report_pdf


router = APIRouter()

@router.post("/{memberGuid}")
def submit_answers(memberGuid: str, answers: List[AnswerSchema], db: db_dependency):
    memberServices.setAsAnsweredMember(memberGuid, db)
    return answersServices.submitAnswers(answers, db)

@router.get("/averages")
def get_averages(db: db_dependency):
    return analyticsServices.getAverage(db)

@router.get("/averages/report")
def get_report(db: db_dependency):
    data = analyticsServices.getAverage(db)
    buffer = generate_survey_report_pdf(data)

    return StreamingResponse(buffer, media_type='application/pdf', headers={
        "Content-Disposition": "attachment; filename=survey_report.pdf"
    })