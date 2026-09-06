from decimal import Decimal

from app.models import ExerciseType, WeightUnit


class ExerciseSetValidationError(ValueError):
    """Raised when exercise set values are invalid."""


def validate_exercise_set_values(
    exercise_type: ExerciseType,
    *,
    set_number: int,
    weight: Decimal | None,
    weight_unit: WeightUnit | None,
    reps: int | None,
    duration_seconds: int | None,
    assistance_weight: Decimal | None,
    assistance_weight_unit: WeightUnit | None,
) -> None:
    
    # first check basic inputs
    validate_basic_set_values(
        set_number=set_number,
        weight=weight,
        reps=reps,
        duration_seconds=duration_seconds,
        assistance_weight=assistance_weight,
    )

    # check specific types

    if exercise_type == ExerciseType.WEIGHTED:
        validate_weighted_set(
            weight=weight,
            weight_unit=weight_unit,
            reps=reps,
            duration_seconds=duration_seconds,
            assistance_weight=assistance_weight,
            assistance_weight_unit=assistance_weight_unit,
        )

    elif exercise_type == ExerciseType.BODYWEIGHT:
        validate_bodyweight_set(
            weight=weight,
            weight_unit=weight_unit,
            reps=reps,
            duration_seconds=duration_seconds,
            assistance_weight=assistance_weight,
            assistance_weight_unit=assistance_weight_unit,
        )

    elif exercise_type == ExerciseType.ASSISTED:
        validate_assisted_set(
            weight=weight,
            weight_unit=weight_unit,
            reps=reps,
            duration_seconds=duration_seconds,
            assistance_weight=assistance_weight,
            assistance_weight_unit=assistance_weight_unit,
        )

    elif exercise_type == ExerciseType.DURATION:
        validate_duration_set(
            weight=weight,
            weight_unit=weight_unit,
            reps=reps,
            duration_seconds=duration_seconds,
            assistance_weight=assistance_weight,
            assistance_weight_unit=assistance_weight_unit,
        )

    else:
        raise ExerciseSetValidationError(
            f"Validation - Unsupported exercise type: {exercise_type}"
        )

    
def validate_basic_set_values(
    *,
    set_number: int,
    weight: Decimal | None,
    reps: int | None,
    duration_seconds: int | None,
    assistance_weight: Decimal | None,
) -> None:
    if set_number < 1:
        raise ExerciseSetValidationError(
            "set_number must be at least 1"
        )

    if weight is not None and weight < 0:
        raise ExerciseSetValidationError(
            "weight cannot be negative"
        )

    if reps is not None and reps < 1:
        raise ExerciseSetValidationError(
            "reps must be at least 1"
        )

    if duration_seconds is not None and duration_seconds < 1:
        raise ExerciseSetValidationError(
            "duration_seconds must be at least 1"
        )

    if assistance_weight is not None and assistance_weight < 0:
        raise ExerciseSetValidationError(
            "assistance_weight cannot be negative"
        )


def validate_weighted_set(
    *,
    weight: Decimal | None,
    weight_unit: WeightUnit | None,
    reps: int | None,
    duration_seconds: int | None,
    assistance_weight: Decimal | None,
    assistance_weight_unit: WeightUnit | None,
) -> None:
    if weight is None:
        raise ExerciseSetValidationError(
            "Weighted exercise requires weight"
        )

    if weight_unit is None:
        raise ExerciseSetValidationError(
            "Weighted exercise requires weight_unit"
        )

    if reps is None:
        raise ExerciseSetValidationError(
            "Weighted exercise requires reps"
        )

    if duration_seconds is not None:
        raise ExerciseSetValidationError(
            "Weighted exercise cannot have duration_seconds"
        )

    if assistance_weight is not None:
        raise ExerciseSetValidationError(
            "Weighted exercise cannot have assistance_weight"
        )

    if assistance_weight_unit is not None:
        raise ExerciseSetValidationError(
            "Weighted exercise cannot have assistance_weight_unit"
        )

def validate_bodyweight_set(
    *,
    weight: Decimal | None,
    weight_unit: WeightUnit | None,
    reps: int | None,
    duration_seconds: int | None,
    assistance_weight: Decimal | None,
    assistance_weight_unit: WeightUnit | None,
) -> None:
    if reps is None:
        raise ExerciseSetValidationError(
            "Bodyweight exercise requires reps"
        )

    if weight is not None:
        raise ExerciseSetValidationError(
            "Bodyweight exercise cannot have weight"
        )

    if weight_unit is not None:
        raise ExerciseSetValidationError(
            "Bodyweight exercise cannot have weight_unit"
        )

    if duration_seconds is not None:
        raise ExerciseSetValidationError(
            "Bodyweight exercise cannot have duration_seconds"
        )

    if assistance_weight is not None:
        raise ExerciseSetValidationError(
            "Bodyweight exercise cannot have assistance_weight"
        )

    if assistance_weight_unit is not None:
        raise ExerciseSetValidationError(
            "Bodyweight exercise cannot have assistance_weight_unit"
        )
    
def validate_assisted_set(
    *,
    weight: Decimal | None,
    weight_unit: WeightUnit | None,
    reps: int | None,
    duration_seconds: int | None,
    assistance_weight: Decimal | None,
    assistance_weight_unit: WeightUnit | None,
) -> None:
    if assistance_weight is None:
        raise ExerciseSetValidationError(
            "Assisted exercise requires assistance_weight"
        )

    if assistance_weight_unit is None:
        raise ExerciseSetValidationError(
            "Assisted exercise requires assistance_weight_unit"
        )

    if reps is None:
        raise ExerciseSetValidationError(
            "Assisted exercise requires reps"
        )

    if weight is not None:
        raise ExerciseSetValidationError(
            "Assisted exercise cannot have weight"
        )

    if weight_unit is not None:
        raise ExerciseSetValidationError(
            "Assisted exercise cannot have weight_unit"
        )

    if duration_seconds is not None:
        raise ExerciseSetValidationError(
            "Assisted exercise cannot have duration_seconds"
        )
    
def validate_duration_set(
    *,
    weight: Decimal | None,
    weight_unit: WeightUnit | None,
    reps: int | None,
    duration_seconds: int | None,
    assistance_weight: Decimal | None,
    assistance_weight_unit: WeightUnit | None,
) -> None:
    if duration_seconds is None:
        raise ExerciseSetValidationError(
            "Duration exercise requires duration_seconds"
        )

    if weight is not None:
        raise ExerciseSetValidationError(
            "Duration exercise cannot have weight"
        )

    if weight_unit is not None:
        raise ExerciseSetValidationError(
            "Duration exercise cannot have weight_unit"
        )

    if reps is not None:
        raise ExerciseSetValidationError(
            "Duration exercise cannot have reps"
        )

    if assistance_weight is not None:
        raise ExerciseSetValidationError(
            "Duration exercise cannot have assistance_weight"
        )

    if assistance_weight_unit is not None:
        raise ExerciseSetValidationError(
            "Duration exercise cannot have assistance_weight_unit"
        )
