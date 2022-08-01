from typing import List
from pydantic import BaseModel, Field

from app.utils.common_models import PaginateItems, Partial


# Subject
class SubjectBase(BaseModel):
    title: str = Field(..., title="Title", description="Subject title")
    level: str = Field(...,
                       title="Level",
                       description="Subject level",
                       min_length=1,
                       max_length=1)
    icon_path: str = Field(...,
                           title="Icon path",
                           description="Subject icon path")


class SubjectCreate(SubjectBase):
    pass


class SubjectUpdate(SubjectCreate, metaclass=Partial):
    pass


class SubjectModel(SubjectBase):

    class Config:
        orm_mode = True


class PaginateSubjects(PaginateItems):
    items: List[SubjectModel] = Field(..., description="List of subjects")


# User Subject
class UserSubjectBase(BaseModel):
    semester_id: int = Field(...,
                             title="Semester id",
                             description="User semester id")
    user_id: int = Field(..., title="User id", description="User id")
    subject_id: int = Field(..., title="Subject id", description="Subject id")


class UserSubjectCreate(UserSubjectBase):
    pass


class UserSubjectUpdate(UserSubjectCreate, metaclass=Partial):
    total_score: int = Field(...,
                             title="Total score",
                             description="Total score")
