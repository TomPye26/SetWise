from pydantic import BaseModel


class WorkoutExerciseCreate(BaseModel):
    exercise_id: int
    position: int


class WorkoutExerciseResponse(BaseModel):
    workout_id: int
    exercise_id: int
    position: int

    model_config = {"from_attributes": True}
