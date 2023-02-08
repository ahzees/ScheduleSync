from sqlalchemy.orm import Session
from .models.models import *
from schedulesync.core.schemas.schema import CreateOccupation


def get_occupation_list(db: Session):
    return db.query(Occupation).all()


def create_occupation(db: Session, item: CreateOccupation):
    occupation = Occupation(**item.dict())
    db.add(occupation)
    db.commit()
    db.refresh(occupation)
    return occupation


def delete_occupation(db: Session, id: int):
    db.query(Occupation).filter(Occupation.id == id).\
        delete(synchronize_session=False)
    db.commit()
    return {}


def get_occupation(db: Session, id: int):
    return db.query(Occupation).filter(Occupation.id == id).first()


# def get_employee_list(db: Session):
#     employees = db.query(Employee).all()
#     return employees
