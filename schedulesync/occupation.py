from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from core.service import get_occupation_list, create_occupation, delete_occupation as d_ocupation, get_occupation
from core.utils import get_db
from schedulesync.core.schemas.schema import CreateOccupation


router = APIRouter()


@router.get('/', status_code=200)
def get_occupation_list(db: Session = Depends(get_db)):
    occupation_list = get_occupation_list(db)
    return occupation_list


@router.get('/{id}', status_code=200)
def get_occupation(id: int, db: Session = Depends(get_db)):
    return get_occupation(id=id, db=db)


@router.post('/', status_code=201)
def create_occupation(item: CreateOccupation, db: Session = Depends(get_db)):
    return create_occupation(db, item)


@router.delete('/{id}', status_code=200)
def delete_occupation(id: int, db: Session = Depends(get_db)):
    return d_ocupation(db, id)

