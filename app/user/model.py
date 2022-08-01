import json
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash

from app.config.database import Base
from app.user.schema import UserCreate, UserUpdate


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    username = Column(String(255), unique=True, index=True, nullable=False)
    __password = Column('hashed_password', String(255), nullable=False)
    user_subjects = relationship('UserSubject', back_populates='users')

    def __init__(self, user_in: UserCreate):
        self.update(user_in)

    def update(self, user_in: UserUpdate):
        self.email = user_in.email or self.email
        self.first_name = user_in.first_name or self.first_name
        self.last_name = user_in.last_name or self.last_name
        self.username = user_in.username or self.username
        self.password = user_in.password or self.__password

    @property
    def password(self):
        return '*' * 8

    @password.setter
    def password(self, password: str):
        self.__password = generate_password_hash(password)

    def __repr__(self) -> str:
        _repr = json.dumps(self.__dict__)
        return _repr
