from pydantic import BaseModel

from typing import Optional
from datetime import datetime


class QuestionResponse(BaseModel):
    id: int
    owner_id: int
    title: str
    description: Optional[str] = None
    topic_id: int
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "example": {
                "title": "Question",
                "description": "Question description",

            }
        }
    }


class QuestionCreate(BaseModel):
    title: str
    description: Optional[str] = None
    topic_id: int


class QuestionUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    topic_id: int
