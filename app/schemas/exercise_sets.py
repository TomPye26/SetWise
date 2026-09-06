from decimal import Decimal

from pydantic import BaseModel

from app.models import WeightUnit


class ExerciseSetCreate(BaseModel):
    exercise_id: int
    set_number: int

    weight: Decimal | None = None
    weight_unit: WeightUnit | None = None

    reps: int | None = None

    duration_seconds: int | None = None

    assistance_weight: Decimal | None = None
    assistance_weight_unit: WeightUnit | None = None


class ExerciseSetUpdate(BaseModel):
    set_number: int | None = None

    weight: Decimal | None = None
    weight_unit: WeightUnit | None = None

    reps: int | None = None

    duration_seconds: int | None = None

    assistance_weight: Decimal | None = None
    assistance_weight_unit: WeightUnit | None = None


class ExerciseSetResponse(BaseModel):
    id: int
    session_id: int
    exercise_id: int
    set_number: int

    weight: Decimal | None
    weight_unit: WeightUnit | None

    reps: int | None

    duration_seconds: int | None

    assistance_weight: Decimal | None
    assistance_weight_unit: WeightUnit | None

    model_config = {"from_attributes": True}
