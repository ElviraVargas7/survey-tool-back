import models
import logging
import uuid 
from sqlalchemy.orm import Session
from db.schema import Members

def getMembers(db: Session):
    return db.query(models.Members).all()

def addMember(member: Members, db: Session):
    dbMember = db.query(models.Members).filter(models.Members.email == member.email).first()
    if dbMember is None:
        logging.info(f"Creating new member for {member.email}")
        newUuid = str(uuid.uuid4())
        dbMember = models.Members(id=newUuid, name=member.name, email=member.email)
        db.add(dbMember)
        db.commit()
        db.refresh(dbMember)
    else:
        logging.error("Member already exists")
        raise Exception("Member already exists")
    
    return dbMember

def deleteMember(email: str, db: Session):
    dbMember = db.query(models.Members).filter(models.Members.email == email).first()
    if dbMember is None:
        logging.error(f"Member with email {email} not found")
        raise Exception("Member not found")
    
    logging.info(f"Deleting member with email {email}")
    db.delete(dbMember)
    db.commit()
    return {"message": f"Member with email {email} deleted successfully"}

def updateMember(email: str, updated_data: Members, db: Session):
    dbMember = db.query(models.Members).filter(models.Members.email == email).first()
    if dbMember is None:
        logging.error(f"Member with email {email} not found")
        raise Exception("Member not found")

    logging.info(f"Updating member with email {email}")
    
    dbMember.name = updated_data.name
    dbMember.email = updated_data.email

    db.commit()
    db.refresh(dbMember)
    
    return dbMember