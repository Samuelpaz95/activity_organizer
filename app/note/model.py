from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, Text

from app.config.database import Base
from app.note.schema import NoteCreate


class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    create_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    update_at = Column(DateTime,
                       nullable=False,
                       default=datetime.utcnow,
                       onupdate=datetime.utcnow)

    def __init__(self, note: NoteCreate) -> None:
        self.update(note)

    def update(self, note: NoteCreate) -> None:
        self.content = note.content or self.content
