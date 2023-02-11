from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schedulesync.core.schemas.schema import CreateOccupation
from schedulesync.core.service import create_occupation as c_occupation
from schedulesync.core.service import delete_occupation as d_ocupation
from schedulesync.core.service import get_occupation as g_occupation
from schedulesync.core.service import get_occupation_list as g_occupation_list
from schedulesync.core.utils import get_db

router = APIRouter()


@router.get("/", status_code=200, summary="Get list of occupation`s")
async def get_occupation_list(db: Session = Depends(get_db)):
    occupation_list = g_occupation_list(db)
    return occupation_list


@router.get("/{id}", status_code=200, summary="Get specific occupation")
async def get_occupation(id: int, db: Session = Depends(get_db)):
    return g_occupation(id=id, db=db)


@router.post("/", status_code=201, summary="Create occupation")
async def create_occupation(item: CreateOccupation, db: Session = Depends(get_db)):
    return c_occupation(db, item)


@router.delete("/{id}", status_code=200, summary="Delete occupation")
async def delete_occupation(id: int, db: Session = Depends(get_db)):
    return d_ocupation(db, id)
