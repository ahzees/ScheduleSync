from fastapi import APIRouter, Depends
from fastapi_users import FastAPIUsers

from schedulesync import employee, occupation, shift
from schedulesync.core.auth.auth import auth_backend
from schedulesync.core.auth.manager import get_user_manager
from schedulesync.core.models.models import User
from schedulesync.core.schemas.schema import UserCreate, UserRead

routes = APIRouter()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
current_user = fastapi_users.current_user()


@routes.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return {"Hello": user.email}


routes.include_router(occupation.router, prefix="/occupation")
routes.include_router(employee.router, prefix="/employee")
routes.include_router(shift.router, prefix="/shift")
routes.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
routes.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
