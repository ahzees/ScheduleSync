from fastapi import APIRouter

from schedulesync import employee, occupation

routes = APIRouter()

routes.include_router(occupation.router, prefix="/occupation")
routes.include_router(employee.router, prefix="/employee")
