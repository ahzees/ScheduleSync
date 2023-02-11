from datetime import date

from pydantic import BaseModel


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
