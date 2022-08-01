from typing import Optional

from pydantic import BaseModel, Field

from app.utils.common_models import Partial


class ActivityBase(BaseModel):
    start_date: str = Field(...,
                            title="Start date",
                            description="Activity start date")
    end_date: str = Field(...,
                          title="End date",
                          description="Activity end date")
    content: str = Field(..., title="Content", description="Activity content")
    score: Optional[str] = Field(None,
                                 title="Score",
                                 description="Activity score")
    is_template: bool = Field(False,
                              title="Is template",
                              description="Is template")
    status_id: int = Field(...,
                           title="Status id",
                           description="Activity status id")
    activity_type_id: int = Field(...,
                                  title="Activity type id",
                                  description="Activity type id")


class ActivityCreate(ActivityBase):
    pass


class ActivityUpdate(ActivityCreate, metaclass=Partial):
    pass


class ActivityModel(ActivityBase):

    class Config:
        orm_mode = True
