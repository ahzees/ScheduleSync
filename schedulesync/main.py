from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response

from schedulesync.core.auth.db import async_session_maker
from schedulesync.routes import routes

tags_metadata = [
    {
        "name": "Employee",
        "description": "Operations with employeers",
    },
    {
        "name": "Occupation",
        "description": "Manage items. So _fancy_ they have their own docs.",
    },
    {
        "name": "Shift",
        "description": "Operatioins with shifts",
    },
]

app = FastAPI(openapi_tags=tags_metadata)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = async_session_maker()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


app.include_router(routes)
