from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy import delete, insert, select
from sqlalchemy.orm import Session

from schedulesync.core.auth.db import get_async_session
from schedulesync.core.models.models import Shift
from schedulesync.core.schemas.schema import Shift as ShiftSchema

router = APIRouter()


@router.get("/", status_code=200, summary="Get shift`s list", tags=["Shift"])
async def get_shifts(db: Session = Depends(get_async_session)):
    return (await db.execute(select(Shift))).scalars().all()


@router.get("/{id}", status_code=200, summary="Get shift", tags=["Shift"])
async def get_shift(id: int, db: Session = Depends(get_async_session)):
    if await db.scalar(select(Shift).where(Shift.id == id)):
        return (await db.execute(select(Shift).where(Shift.id == id))).scalars().all()
    return JSONResponse({"status": "Not found"}, status_code=404)


@router.get(
    "/employee/{employee_id}",
    status_code=200,
    summary="Get the work shift of an employee",
    tags=["Shift"],
)
async def get_employee_shift(id: int, db: Session = Depends(get_async_session)):
    if await db.scalar(select(Shift).where(Shift.employee_id == id)):
        return (
            (await db.execute(select(Shift).where(Shift.employee_id == id)))
            .scalars()
            .one()
        )
    return JSONResponse({"status": "Not found"}, status_code=404)


@router.post("/", status_code=201, summary="Create shift", tags=["Shift"])
async def create_shift(item: ShiftSchema, db: Session = Depends(get_async_session)):
    shift = insert(Shift).values(**item.dict()).returning(Shift.id)
    result = await db.execute(shift)
    await db.commit()
    return (
        await db.execute(select(Shift).where(Shift.id == result.scalar_one()))
    ).scalar_one()


@router.delete("/{id}", summary="Delete shift", tags=["Shift"])
async def delete_shift(id: int, db: Session = Depends(get_async_session)):
    await db.execute(delete(Shift).where(Shift.id == id))
    await db.commit()
    return JSONResponse({"status": "succesful"}, status_code=204)


@router.delete(
    "/employee/{id}", summary="Delete the work shift of an employee", tags=["Shift"]
)
async def delete_employee_shift(id: int, db: Session = Depends(get_async_session)):
    await db.execute(delete(Shift).where(Shift.employee_id == id))
    await db.commit()
    return JSONResponse({"status": "succesful"}, status_code=204)
