import os
import uuid
from typing import Optional

from dotenv import load_dotenv
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin

from .db import User, get_user_db

load_dotenv()
SECRET2 = os.getenv("SECRET1")


class UserManager(IntegerIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET2
    verification_token_secret = SECRET2

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
