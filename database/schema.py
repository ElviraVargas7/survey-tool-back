from pydantic import BaseModel

class Members(BaseModel):
    id: str
    name: str
    email: str
    has_answers: bool

class Question(BaseModel):
    id: str
    question: str

#no memberId do it is annonymous
class Answers(BaseModel):
    id: str
    questionId: str
    rate: float