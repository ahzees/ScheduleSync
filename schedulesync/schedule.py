from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from core.utils import get_db

router = APIRouter()


@router.get('/')
def list(db: Session = Depends(get_db)):
    print(db)
    return {}
