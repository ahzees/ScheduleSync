from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic.error_wrappers import ValidationError
from sqlalchemy import insert, select, update
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session, selectinload

from schedulesync.core.auth.db import get_async_session
from schedulesync.core.models.models import Employee
from schedulesync.core.schemas.schema import CreateEmployee as CreateEmployeeSchema
from schedulesync.core.schemas.schema import Employee as EmployeeSchema
from schedulesync.core.schemas.schema import PutUpdateEmployee

router = APIRouter()


@router.get("/", status_code=200, tags=["Employee"])
async def get_employee_list(db: Session = Depends(get_async_session)):
    result = select(Employee)
    result = await db.execute(result)
    return result.scalars().all()


@router.get("/{id}", status_code=200, tags=["Employee"])
async def get_employee(id: int, db: Session = Depends(get_async_session)):
    result = select(Employee).where(Employee.id == id)
    result = await db.execute(result)
    try:
        return result.scalar_one()
    except NoResultFound:
        return JSONResponse({"error": "object not found"}, status_code=404)


@router.post("/", status_code=201, tags=["Employee"])
async def create_employee(
    item: CreateEmployeeSchema, db: Session = Depends(get_async_session)
):
    employee = insert(Employee).values(**item.dict()).returning(Employee.id)
    result = await db.execute(employee)
    await db.commit()
    return (
        await db.execute(select(Employee).where(Employee.id == result.scalar_one()))
    ).scalar_one()


@router.delete("/{id}", status_code=200, tags=["Employee"])
async def delete_employee(id: int, db: Session = Depends(get_async_session)):
    try:
        result = await db.execute(select(Employee).where(Employee.id == id))
        await db.delete(result.scalar_one())
        await db.commit()
        return JSONResponse({"status": "succesful"}, status_code=204)
    except NoResultFound:
        return JSONResponse({"error": "object not found"}, status_code=404)


@router.put("/{id}", tags=["Employee"])
async def put_update_employee(
    id: int, item: EmployeeSchema, db: Session = Depends(get_async_session)
):
    try:
        _update = (
            update(Employee)
            .where(Employee.id == id)
            .values(**item.dict())
            .returning(Employee)
        )
        result = await db.execute(_update)
        await db.commit()
        return result.scalar_one()
    except NoResultFound:
        return JSONResponse({"error": "object not found"}, status_code=404)


@router.patch("/{id}", tags=["Employee"])
async def patch_update_employee(
    id: int, item: PutUpdateEmployee, db: Session = Depends(get_async_session)
):
    try:
        dct = {}
        for i in item.__dict__:
            if item.__dict__[i] != None:
                dct[i] = item.__dict__[i]
        print(dct)
        _update = (
            update(Employee).where(Employee.id == id).values(dct).returning(Employee)
        )
        result = await db.execute(_update)
        await db.commit()
        return result.scalar_one()
    except NoResultFound:
        return JSONResponse({"error": "object not found"}, status_code=404)
