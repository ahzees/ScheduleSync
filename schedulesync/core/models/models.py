from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .db import Base


class Occupation(Base):
    __tablename__ = "occupation"
    id = Column(Integer, primary_key=True, unique=True, index=True)
    title = Column(String(250), unique=True)


class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True, unique=True, index=True)
    email = Column(String(250))
    phone_number = Column(String(15))
    first_name = Column(String(100))
    last_name = Column(String(100))
    date_of_birth = Column(Date)
    occupation_id = Column(Integer, ForeignKey("occupation.id"))


class Shift(Base):
    __tablename__ = "shift"
    employee_id = Column(
        Integer, ForeignKey("employee.id"), primary_key=True, index=True, unique=True
    )
    id = Column(Integer)


class Policy(Base):
    __tablename__ = "policy"
    id = Column(
        Integer,
        primary_key=True,
        index=True,
        unique=True,
    )
    working_hours_amount = Column(Integer)
    holidays = Column(String(300))
    vacation_amount = Column(Integer)
    sick_leaves_amount = Column(Integer)
    time_off_amount = Column(Integer)


class Timetable(Base):
    __tablename__ = "timetable"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    occupation_id = Column(Integer, ForeignKey("occupation.id"))
    shift_id = Column(Integer, ForeignKey("shift.employee_id"))
    policy_id = Column(Integer, ForeignKey("policy.id"))
    working_days = Column(String(250))
    working_hours = Column(String(100))


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, unique=True, index=True)
    email = Column(String(150), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
