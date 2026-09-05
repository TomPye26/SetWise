from datetime import datetime

from pydantic import BaseModel


class WorkoutCreate(BaseModel):
    user_id: int
    name: str


class WorkoutUpdate(BaseModel):
    name: str


class WorkoutResponse(BaseModel):
    id: int
    user_id: int
    name: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }
