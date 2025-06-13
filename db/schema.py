from typing import Optional
from pydantic import BaseModel
from uuid import UUID

class Members(BaseModel):
    id: UUID
    name: str
    email: str
    has_answers: bool

class Questions(BaseModel):
    id: int
    question: str

#no memberId do it is annonymous
class Answers(BaseModel):
    id: Optional[int] = None 
    questionId: int
    rate: float