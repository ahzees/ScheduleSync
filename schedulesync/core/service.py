from fastapi import HTTPException
from sqlalchemy import update
from sqlalchemy.orm import Session

from schedulesync.core.models.models import Employee, Occupation, Shift
from schedulesync.core.schemas.schema import CreateEmployee, CreateOccupation
from schedulesync.core.schemas.schema import Shift as ShiftSchema


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
    db.execute(update(Employee).where(Employee.id == id).values(**item.dict()))
    db.commit()
    return item


def get_shift_list(db: Session):
    return db.query(Shift).all()


def create_shift(db: Session, item: ShiftSchema):
    shift = Shift(**item.dict())
    db.add(shift)
    db.commit()
    db.refresh(shift)
    return shift


def get_shift(db: Session, id: int):
    return db.query(Shift).filter(Shift.id == id).all()


def delete_shift(db: Session, id: int):
    db.query(Shift).filter(Shift.employee_id == id).delete()
    db.commit()
    return {}


def get_shift_by_employeer(db: Session, id: int):
    return db.query(Shift).filter(Shift.employee_id == id).one()


def delete_specific_shift(db: Session, id: int):
    for i in db.query(Shift).filter(Shift.id == id):
        db.delete(i)
    db.commit()
    return {}
