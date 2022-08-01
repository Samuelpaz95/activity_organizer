from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import relationship

from app.config.database import Base


class Semester(Base):
    __tablename__ = 'semesters'
    id = Column(Integer, primary_key=True, index=True)
    gestion = Column(String(10), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    user_subjects = relationship('UserSubject', back_populates='semesters')

    def __init__(self, gestion: str, end_date: Date):
        self.update(self, gestion=gestion, end_date=end_date)

    def update(self, gestion: str, end_date: Date):
        self.gestion = gestion or self.gestion
        self.start_date = self.start_date or self.start_date
        self.end_date = end_date or self.end_date

    def __repr__(self):
        return f'<Semester {self.gestion}>'