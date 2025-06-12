from sqlalchemy import Boolean, Column, ForeignKey, String, Integer, Float
from database import Base

class Members(Base):
    __tablename__ = "members"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    has_answers = Column(Boolean, default=False)

class Questions(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, index=True)

#no memberId do it is annonymous
class Answers(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True)
    questionId = Column(Integer, ForeignKey("quesitions.id"), index=True)
    rate = Column(Float, index=True)
