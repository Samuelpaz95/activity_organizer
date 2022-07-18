from typing import List
from pydantic import BaseModel, EmailStr, Field

from app.utils.common_models import PaginateItems, Partial


class UserBase(BaseModel):
    email: EmailStr = Field(..., title="Email", description="User email")

    username: str = Field(...,
                          min_length=8,
                          max_length=255,
                          description="User username")

    first_name: str = Field(...,
                            min_length=1,
                            max_length=255,
                            description="User first name")

    last_name: str = Field(...,
                           min_length=1,
                           max_length=255,
                           description="User last name")


class UserCreate(UserBase):
    password: str = Field(...,
                          title="User password",
                          min_length=8,
                          max_length=128,
                          description="User password")


class UserUpdate(UserCreate, metaclass=Partial):
    pass


class UserModel(UserBase):

    class Config:
        orm_mode = True


class PaginateUsers(PaginateItems):
    items: List[UserModel] = Field(..., description="List of users")
