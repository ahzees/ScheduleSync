from fastapi import APIRouter, Depends, HTTPException, Query
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


@router.get("/", status_code=200, summary="Get shift`s list", tags=["Shift"])
def get_shift_list(db: Session = Depends(get_db)):
    return g_shift_list(db)


@router.post("/", status_code=201, summary="Create shift", tags=["Shift"])
def create_shift(item: ShiftSchema, db: Session = Depends(get_db)):
    return c_shift(db, item)


# @router.delete("/{id}", summary="Delete shift in specific employeer")
# def delete_shift(id: int, db: Session = Depends(get_db)):
#     return d_shift(db=db, id=id)


@router.get(
    "/by/{id}",
    status_code=200,
    summary="Get specific shift",
    tags=["Shift"],
    description="If u want to get specific employeer from shifts -> {employee_id}?q=employee<br>"
    "If u want to get all employeers from specific shift -> {shift_id}?q=shift",
)
def get_shift(
    id: int = 0,
    q=Query(
        "shift",
        description="description goes here",
    ),
    db: Session = Depends(get_db),
):
    if q == "employee":
        return g_shift_by_employeer(db=db, id=id)
    if q == "shift":
        return g_shift(db=db, id=id)
    return HTTPException(status_code=404)


# @router.get("/{employee_id}", status_code=200, summary="Get shift by employeer")
# def get_shift_by_employeer(employee_id: int, db: Session = Depends(get_db)):
#     return g_shift_by_employeer(db=db, id=employee_id)


@router.delete(
    "/{id}",
    summary="Delete specific shift",
    tags=["Shift"],
    description="If u want to delete the shift -> {shift_id}?q=shift<br>"
    "If u want to delete employee from shifts -> {employee_id}?q=employee",
)
def delete_specific_shift(id: int, q=None, db: Session = Depends(get_db)):
    if q == "shift":
        return d_specific_shift(id=id, db=db)
    else:
        return d_shift(db=db, id=id)
