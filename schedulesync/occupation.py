from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy import delete, insert, select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from schedulesync.core.auth.db import get_async_session
from schedulesync.core.models.models import Occupation
from schedulesync.core.schemas.schema import CreateOccupation

router = APIRouter()


@router.get(
    "/", status_code=200, summary="Get list of occupation`s", tags=["Occupation"]
)
async def get_occupation_list(db: Session = Depends(get_async_session)):
    occupation_list = select(Occupation)
    result = await db.execute(occupation_list)
    return result.scalars().all()


@router.get(
    "/{id}", status_code=200, summary="Get specific occupation", tags=["Occupation"]
)
async def get_occupation(id: int, db: Session = Depends(get_async_session)):
    occupation = select(Occupation).where(Occupation.id == id)
    result = await db.execute(occupation)
    try:
        return result.scalar_one()
    except NoResultFound:
        raise HTTPException(status_code=404)


@router.post("/", status_code=201, summary="Create occupation", tags=["Occupation"])
async def create_occupation(
    item: CreateOccupation, db: Session = Depends(get_async_session)
):
    occupation = insert(Occupation).values(**item.dict())
    await db.execute(occupation)
    await db.commit()
    return {"status": "succesful"}


@router.delete(
    "/{id}", status_code=200, summary="Delete occupation", tags=["Occupation"]
)
async def delete_occupation(id: int, db: Session = Depends(get_async_session)):
    await db.execute(delete(Occupation).where(Occupation.id == id))
    await db.commit()
    return {"status": "succescful"}
