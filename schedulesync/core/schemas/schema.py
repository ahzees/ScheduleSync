from pydantic import BaseModel


class Employee(BaseModel):
    id: int
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class OccupationBase(BaseModel):
    title: str


class OccupationList(BaseModel):
    id: int


class CreateOccupation(OccupationBase):
    ...
