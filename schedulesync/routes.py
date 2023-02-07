from fastapi import APIRouter
from schedulesync import schedule

routes = APIRouter()

routes.include_router(schedule.router, prefix='/schedule')
