from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr


class Employee(BaseModel):
    email: str
    phone_number: str
    first_name: str
    last_name: str
    date_of_birth: date
    occupation_id: int


class CreateEmployee(Employee):
    ...


class OccupationBase(BaseModel):
    title: str


class OccupationList(BaseModel):
    id: int


class CreateOccupation(OccupationBase):
    ...


class Shift(BaseModel):
    employee_id: int
    id: int


from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    pass


class UserCreate(schemas.BaseUserCreate):
    email: EmailStr
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    pass


class PutUpdateEmployee(BaseModel):
    email: Optional[str] = None
    phone_number: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[date] = None
    occupation_id: Optional[int] = None
