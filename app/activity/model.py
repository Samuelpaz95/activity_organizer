from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Date
from sqlalchemy.orm import relationship
from app.activity.schema import ActivityCreate, ActivityUpdate

from app.config.database import Base


class Status(Base):
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    color = Column(String(len('#00000000')), nullable=False)


class ActiviyType(Base):
    __tablename__ = 'activity_types'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    color = Column(String(len('#00000000')), nullable=False)


class Activity(Base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True, index=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    content = Column(Text, nullable=False)
    score = Column(Integer, nullable=True)
    is_template = Column(Boolean, nullable=False, default=False)
    status_id = Column(Integer, ForeignKey('status.id'), nullable=False)
    status = relationship('Status', back_populates='activities')
    activity_type_id = Column(Integer,
                              ForeignKey('activity_types.id'),
                              nullable=False)
    activity_type = relationship('ActiviyType', back_populates='activities')
    user_subject_id = Column(Integer,
                             ForeignKey('user_subjects.id'),
                             nullable=False)
    user_subject = relationship('UserSubject', back_populates='activities')

    def __init__(self, activity: ActivityCreate) -> None:
        self.update(activity)

    def update(self, activity: ActivityUpdate) -> None:
        self.start_date = activity.start_date or self.start_date
        self.end_date = activity.end_date or self.end_date
        self.content = activity.content or self.content
        self.score = activity.score or self.score
        self.is_template = activity.is_template or self.is_template
        self.status_id = activity.status_id or self.status_id
        self.activity_type_id = activity.activity_type_id or self.activity_type_id

    def __repr__(self) -> str:
        _repr = f'<Activity {self.id}\n'
        _repr += f'start_date {self.start_date}\n'
        _repr += f'end_date {self.end_date}\n'
        _repr += f'content {self.content}\n'
        _repr += f'score {self.score}\n'
        _repr += f'is_template {self.is_template}\n'
        _repr += f'status_id {self.status_id}\n'
        _repr += f'activity_type_id {self.activity_type_id}\n'
        _repr += '>'
        return _repr
