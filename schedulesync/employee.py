from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from core.service import get_employee_list as g_employee_list,\
        create_employee as c_employee,\
        get_employee as g_employee, \
        delete_employee as d_employee, \
        update_employee as u_employee
from core.utils import get_db
from schedulesync.core.schemas.schema import CreateOccupation, CreateEmployee, Employee


router = APIRouter()


@router.get('/', status_code=200)
def get_employee_list(db: Session = Depends(get_db)):
    employees = g_employee_list(db)
    return employees


@router.get('/{id}', status_code=200)
def get_employee(id: int, db: Session = Depends(get_db)):
    return g_employee(id=id, db=db)


@router.post('/', status_code=201)
def create_employee(item: CreateEmployee, db: Session = Depends(get_db)):
    return c_employee(db, item)


@router.delete('/{id}', status_code=200)
def delete_employee(id: int, db: Session = Depends(get_db)):
    return d_employee(db, id)


@router.put('/{id}')
def update_employee(id: int, item: Employee, db: Session = Depends(get_db)):
    return u_employee(db=db, id=id, item=item)
