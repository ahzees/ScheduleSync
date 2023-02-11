from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schedulesync.core.schemas.schema import Shift as ShiftSchema
from schedulesync.core.service import create_shift as c_shift
from schedulesync.core.service import delete_shift as d_shift
from schedulesync.core.service import delete_specific_shift as d_specific_shift
from schedulesync.core.service import get_shift as g_shift
from schedulesync.core.service import get_shift_by_employeer as g_shift_by_employeer
from schedulesync.core.service import get_shift_list as g_shift_list
from schedulesync.core.utils import get_db

router = APIRouter()


@router.get("/", status_code=200, summary="Get shift`s list")
def get_shift_list(db: Session = Depends(get_db)):
    return g_shift_list(db)


@router.post("/", status_code=201, summary="Create shift")
def create_shift(item: ShiftSchema, db: Session = Depends(get_db)):
    return c_shift(db, item)


@router.delete("/{id}", summary="Delete shift in specific employeer")
def delete_shift(id: int, db: Session = Depends(get_db)):
    return d_shift(db=db, id=id)


@router.get("/shift/{id}", status_code=200, summary="Get specific shift")
def get_shift(id: int, db: Session = Depends(get_db)):
    return g_shift(db=db, id=id)


@router.get("/{employee_id}", status_code=200, summary="Get shift by employeer")
def get_shift_by_employeer(employee_id: int, db: Session = Depends(get_db)):
    return g_shift_by_employeer(db=db, id=employee_id)


@router.delete("/shift/{id}", summary="Delete specific shift")
def delete_specific_shift(id: int, db: Session = Depends(get_db)):
    return d_specific_shift(id=id, db=db)
