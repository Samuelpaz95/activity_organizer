from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.config.database import Base
from app.subject.schema import SubjectCreate, UserSubjectCreate


class UserSubject(Base):
    __tablename__ = 'user_subjects'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.id'), nullable=False)
    semester_id = Column(Integer, ForeignKey('semesters.id'), nullable=False)
    user = relationship('User', back_populates='user_subjects')
    subject = relationship('Subject', back_populates='user_subjects')
    semester = relationship('Semester', back_populates='user_subjects')

    def __init__(self, user_subject: UserSubjectCreate) -> None:
        self.update(user_subject)

    def update(self, user_subject: UserSubjectCreate) -> None:
        self.user_id = user_subject.user_id or self.user_id
        self.subject_id = user_subject.subject_id or self.subject_id
        self.semester_id = user_subject.semester_id or self.semester_id
        self.total_score = user_subject.total_score or self.total_score


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    level = Column(String(255), nullable=False)
    icon_path = Column(String(255), nullable=False)
    user_subjects = relationship('UserSubject', back_populates='subjects')

    def __init__(self, subject: SubjectCreate) -> None:
        self.update(subject)

    def update(self, subject: SubjectCreate) -> None:
        self.title = subject.title or self.title
        self.level = subject.level or self.level
        self.icon_path = subject.icon_path or self.icon_path