from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schedulesync.core.schemas.schema import CreateEmployee, CreateOccupation, Employee
from schedulesync.core.service import create_employee as c_employee
from schedulesync.core.service import delete_employee as d_employee
from schedulesync.core.service import get_employee as g_employee
from schedulesync.core.service import get_employee_list as g_employee_list
from schedulesync.core.service import update_employee as u_employee
from schedulesync.core.utils import get_db

router = APIRouter()


@router.get("/", status_code=200)
async def get_employee_list(db: Session = Depends(get_db)):
    employees = g_employee_list(db)
    return employees


@router.get("/{id}", status_code=200)
async def get_employee(id: int, db: Session = Depends(get_db)):
    return g_employee(id=id, db=db)


@router.post("/", status_code=201)
async def create_employee(item: CreateEmployee, db: Session = Depends(get_db)):
    return c_employee(db, item)


@router.delete("/{id}", status_code=200)
async def delete_employee(id: int, db: Session = Depends(get_db)):
    return d_employee(db, id)


@router.put("/{id}")
async def update_employee(id: int, item: Employee, db: Session = Depends(get_db)):
    return u_employee(db=db, id=id, item=item)
