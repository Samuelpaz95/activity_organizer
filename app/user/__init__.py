from typing import Optional
from fastapi import APIRouter, Body, Depends, Path, Query, status

from app.user.schema import PaginateUsers, UserCreate, UserModel
from app.user.service import UserService

router = APIRouter()
tags = ["user"]


@router.post("/",
             response_model=UserModel,
             status_code=status.HTTP_201_CREATED,
             tags=tags)
def create_user(user: UserCreate = Body(...),
                service: UserService = Depends()) -> UserModel:
    db_user = service.create_user(user)
    user = UserModel.from_orm(db_user)
    return user


@router.get("/", response_model=PaginateUsers, tags=tags)
def get_users(limit: Optional[int] = Query(10,
                                           get_param="limit",
                                           description="Limit of users"),
              offset: Optional[int] = Query(0,
                                            get_param="offset",
                                            description="Offset of users"),
              service: UserService = Depends()) -> PaginateUsers:
    data = dict(
        items=service.get_users(limit, offset),
        next_page=f'/users?limit={limit}&offset={offset + limit}',
        previous_page=f'/users?limit={limit}&offset={max(0, offset - limit)}')
    return PaginateUsers(**data)


@router.get("/{user_id}", response_model=UserModel, tags=tags)
def get_user_by_id(user_id: int = Path(..., title="User ID"),
                   service: UserService = Depends()) -> UserModel:
    return service.get_user_by_id(user_id)
