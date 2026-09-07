from pydantic import BaseModel


class WorkoutSessionExerciseCreate(BaseModel):
    exercise_id: int
    position: int


class WorkoutSessionExerciseResponse(BaseModel):
    session_id: int
    exercise_id: int
    position: int

    model_config = {"from_attributes": True}
