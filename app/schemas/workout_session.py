from datetime import datetime

from pydantic import BaseModel


class WorkoutSessionCreate(BaseModel):
    user_id: int
    workout_id: int
    started_at: datetime | None = None
    completed_at: datetime | None = None

class WorkoutSessionUpdate(BaseModel):
    completed_at: datetime | None = None


class WorkoutSessionResponse(BaseModel):
    id: int
    user_id: int
    workout_id: int
    started_at: datetime
    completed_at: datetime | None

    model_config = {"from_attributes": True}


