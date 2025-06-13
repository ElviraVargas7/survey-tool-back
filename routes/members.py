import logging
from fastapi import APIRouter
from db.setup import db_dependency
from db.schema import Members as MemberSchema
import services.membersServices as membersServices
from typing import List
from fastapi import HTTPException

router = APIRouter()

@router.get("", response_model=List[MemberSchema])
def get_members(db: db_dependency):
    return membersServices.getMembers(db)

@router.get("/{id}", response_model=MemberSchema)
def get_member_by_id(id: str, db: db_dependency):
    print("id",id)
    return membersServices.getMemberById(id, db)

@router.post("", response_model=MemberSchema)
def create_member(member: MemberSchema, db: db_dependency):
    try:
        return membersServices.addMember(member, db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{email}", response_model=MemberSchema)
def update_member(email: str, updated_data: MemberSchema, db: db_dependency):
    try:
        return membersServices.updateMember(email, updated_data, db)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{email}")
def delete_member(email: str, db: db_dependency):
    try:
        return membersServices.deleteMember(email, db)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
