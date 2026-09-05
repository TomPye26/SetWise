from pydantic import BaseModel

from app.models import ExerciseType


class ExerciseCreate(BaseModel):
    name: str
    muscle_group: str
    exercise_type: ExerciseType


class ExerciseUpdate(BaseModel):
    name: str
    muscle_group: str
    exercise_type: ExerciseType


class ExerciseResponse(BaseModel):
    id: int
    name: str
    muscle_group: str
    exercise_type: ExerciseType

    model_config = {
        "from_attributes": True
    }
