from sqlalchemy.orm import Session
from sqlalchemy import update
from fastapi import HTTPException
from schedulesync.core.models.models import *
from schedulesync.core.schemas.schema import CreateOccupation, CreateEmployee


def get_item(db, id, table):
    return db.query(table).filter(table.id == id).one()


def get_occupation_list(db: Session):
    return db.query(Occupation).all()


def create_occupation(db: Session, item: CreateOccupation):
    occupation = Occupation(**item.dict())
    db.add(occupation)
    db.commit()
    db.refresh(occupation)
    return occupation


def delete_occupation(db: Session, id: int):
    db.query(Occupation).filter(
        Occupation.id == get_item(db, id, Occupation).id
    ).delete()
    db.commit()
    return {}


def get_occupation(db: Session, id: int):
    return get_item(db, id, Occupation)


def get_employee_list(db: Session):
    employees = db.query(Employee).all()
    return employees


def create_employee(db: Session, item: CreateEmployee):
    employee = Employee(**item.dict())
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee


def get_employee(db: Session, id: int):
    return db.query(Employee).filter(Employee.id == id).first()


def delete_employee(db: Session, id: int):
    db.session.delete(get_item(db, id, Employee))
    return {}


def update_employee(id: int, item: CreateEmployee, db: Session):
    print(db.query(Employee).where(Employee.id == id).first())
    db.execute(update(Employee).where(Employee.id == id).values(**item.dict()))
    db.commit()
    return item
