from dataclasses import dataclass
from typing import List

from fastapi import Depends, HTTPException, status
from psycopg2 import IntegrityError
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.user.model import User
from app.user.schema import UserCreate, UserUpdate


@dataclass
class UserService:

    db: Session = Depends(get_db)

    def create_user(self, user: UserCreate) -> User:
        user_db = User(user)
        self.db.add(user_db)
        self.db.commit()
        self.db.refresh(user_db)
        return user_db

    def get_users(self, limit: int = 10, offset: int = 0) -> List[User]:
        return self.db.query(User).limit(limit).offset(offset).all()

    def get_user_by_id(self, user_id: int) -> User:
        user_db = self.db.query(User).get(user_id)
        if user_db is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")
        return self.db.query(User).filter(User.id == user_id).first()

    def update_user(self, user_id: int, user: UserUpdate) -> User:
        user_db = self.get_user_by_id(user_id)
        user_db.update(user)
        self.db.commit()
        self.db.refresh(user_db)
        return user_db

    def remove_user(self, user_id: int) -> User:
        user_db = self.get_user_by_id(user_id)
        self.db.delete(user_db)
        self.db.commit()
        return user_db
