from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from schedulesync.core.auth.db import get_async_session
from schedulesync.core.models.models import Policy
from schedulesync.core.schemas.schema import CreatePolicy as CreatePolicySchema
from schedulesync.core.schemas.schema import PatchUpdatePolicy

router = APIRouter()


@router.get("/", tags=["Policy"])
async def get_policy_list(db: Session = Depends(get_async_session)):
    return (await db.execute(select(Policy))).scalars().all()


@router.get("/{id}", tags=["Policy"])
async def get_policy(id: int, db: Session = Depends(get_async_session)):
    try:
        return (await db.execute(select(Policy).where(Policy.id == id))).scalar_one()
    except NoResultFound:
        return JSONResponse({"error": "object not found"}, status_code=404)


@router.post(
    "/",
    tags=["Policy"],
)
async def create_policy(
    item: CreatePolicySchema, db: Session = Depends(get_async_session)
):
    print(item)
    policy = insert(Policy).values(**item.dict()).returning(Policy.id)
    result = await db.execute(policy)
    await db.commit()
    return (
        await db.execute(select(Policy).where(Policy.id == result.scalar_one()))
    ).scalar_one()


@router.delete(
    "/",
    tags=["Policy"],
)
async def delete_policy(id: int, db: Session = Depends(get_async_session)):
    try:
        result = await db.execute(select(Policy).where(Policy.id == id))
        await db.delete(result.scalar_one())
        await db.commit()
        return JSONResponse({"status": "succesful"}, status_code=204)
    except NoResultFound:
        return JSONResponse({"error": "object not found"}, status_code=404)


@router.patch(
    "/{id}",
    tags=["Policy"],
)
async def update_policy(
    id: int, item: PatchUpdatePolicy, db: Session = Depends(get_async_session)
):
    try:
        dct = {}
        for i in item.__dict__:
            if item.__dict__[i] != None:
                dct[i] = item.__dict__[i]
        _update = update(Policy).where(Policy.id == id).values(dct).returning(Policy)
        result = await db.execute(_update)
        await db.commit()
        return result.scalar_one()
    except NoResultFound:
        return JSONResponse({"error": "object not found"}, status_code=404)
