from pydantic import BaseModel, Field

from app.utils.common_models import Partial


class NoteBase(BaseModel):
    content: str = Field(..., title="Content", description="Note content")
    user_subject_id: int = Field(...,
                                 title="User subject id",
                                 description="Note user subject id")


class NoteCreate(NoteBase):
    pass


class NoteUpdate(NoteCreate, metaclass=Partial):
    pass


class NoteModel(NoteBase):

    class Config:
        orm_mode = True