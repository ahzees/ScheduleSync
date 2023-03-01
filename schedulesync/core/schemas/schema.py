from datetime import date, time
from typing import List, Optional

from pydantic import BaseModel, EmailStr


class Employee(BaseModel):
    email: str
    phone_number: str
    first_name: str
    last_name: str
    date_of_birth: date
    occupation_id: int
    vacation_list: List[date]
    day_off: List[date]
    sick_leaves: List[date]


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


class PatchUpdateEmployee(BaseModel):
    email: Optional[str] = None
    phone_number: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[date] = None
    occupation_id: Optional[int] = None
    vacation_list: Optional[List[date]] = None
    day_off: Optional[List[date]] = None
    sick_leaves: Optional[List[date]] = None


class Policy(BaseModel):
    working_hours_amount: int
    holidays: List[date]
    vacation_amount: int
    sick_leaves_amount: int
    time_off_amount: int
    occupation_id: int


class CreatePolicy(Policy):
    pass


class PatchUpdatePolicy(BaseModel):
    working_hours_amount: Optional[int] = None
    holidays: Optional[List[date]] = None
    vacation_amount: Optional[int] = None
    sick_leaves_amount: Optional[int] = None
    time_off_amount: Optional[int] = None
    occupation_id: Optional[int] = None


class Timetable(BaseModel):
    occupation_id: int
    shift: int
    policy_id: int
    working_days: List[date]
    working_hours: List[time]


class CreateTimetable(BaseModel):
    pass
