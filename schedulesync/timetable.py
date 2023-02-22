from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from schedulesync.core.auth.db import get_async_session
from schedulesync.core.models.models import Timetable
from schedulesync.core.schemas.schema import CreateTimetable
from schedulesync.core.schemas.schema import Timetable as TimetableSchema

router = APIRouter()


@router.get("/", status_code=200, summary="Get list of Timetables", tags=["Timetable"])
async def get_timetable_list(db: Session = Depends(get_async_session)):
    timetable_list = select(Timetable)
    result = await db.execute(timetable_list)
    return result.scalars().all()


@router.get("/{id}", status_code=200, summary="Get Timetable", tags=["Timetable"])
async def get_timetable(id: int, db: Session = Depends(get_async_session)):
    return (await db.execute(select(Timetable).where(Timetable.id == id))).scalar_one()


@router.post("/", status_code=201, summary="Create Timetable", tags=["Timetable"])
async def create_timetable(
    item: TimetableSchema, db: Session = Depends(get_async_session)
):
    timetable = insert(Timetable).values(**item.dict()).returning(Timetable.id)
    result = await db.execute(timetable)
    await db.commit()
    return (
        await db.execute(select(Timetable).where(Timetable.id == result.scalar_one()))
    ).scalar_one()


@router.delete("/{id}", status_code=201, summary="Delete Timetable", tags=["Timetable"])
async def delete_policy(id: int, db: Session = Depends(get_async_session)):
    try:
        result = await db.execute(select(Timetable).where(Timetable.id == id))
        await db.delete(result.scalar_one())
        await db.commit()
        return JSONResponse({"status": "succesful"}, status_code=204)
    except NoResultFound:
        return JSONResponse({"error": "object not found"}, status_code=404)
