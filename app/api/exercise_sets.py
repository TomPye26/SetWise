from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models import Exercise, ExerciseSet, WorkoutSession
from app.schemas import (
    ExerciseSetCreate,
    ExerciseSetResponse,
    ExerciseSetUpdate,
)
from app.services.exercise_set_validation import (
    ExerciseSetValidationError,
    validate_exercise_set_values,
)

router = APIRouter(
    prefix="/exercise-sets",
    tags=["exercise-sets"],
)


@router.get(
    "/session/{session_id}",
    response_model=list[ExerciseSetResponse],
)
def get_exercise_sets(
    session_id: int,
    db: Session = Depends(get_db),
):
    session = db.get(WorkoutSession, session_id)

    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Workout session not found",
        )

    return (
        db.query(ExerciseSet)
        .filter(ExerciseSet.session_id == session_id)
        .order_by(
            ExerciseSet.exercise_id,
            ExerciseSet.set_number,
        )
        .all()
    )


@router.get(
    "/{set_id}",
    response_model=ExerciseSetResponse,
)
def get_exercise_set(
    set_id: int,
    db: Session = Depends(get_db),
):
    exercise_set = db.get(ExerciseSet, set_id)

    if exercise_set is None:
        raise HTTPException(
            status_code=404,
            detail="Exercise set not found",
        )

    return exercise_set


@router.post(
    "/session/{session_id}",
    response_model=ExerciseSetResponse,
)
def create_exercise_set(
    session_id: int,
    set_data: ExerciseSetCreate,
    db: Session = Depends(get_db),
):
    session = db.get(WorkoutSession, session_id)

    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Workout session not found",
        )

    exercise = db.get(Exercise, set_data.exercise_id)

    if exercise is None:
        raise HTTPException(
            status_code=404,
            detail="Exercise not found",
        )

    try:
        validate_exercise_set_values(
            exercise.exercise_type,
            set_number=set_data.set_number,
            weight=set_data.weight,
            weight_unit=set_data.weight_unit,
            reps=set_data.reps,
            duration_seconds=set_data.duration_seconds,
            assistance_weight=set_data.assistance_weight,
            assistance_weight_unit=set_data.assistance_weight_unit,
        )
    except ExerciseSetValidationError as exc:
        raise HTTPException(
            status_code=422,
            detail=str(exc),
        )

    exercise_set = ExerciseSet(
        session_id=session_id,
        exercise_id=set_data.exercise_id,
        set_number=set_data.set_number,
        weight=set_data.weight,
        weight_unit=set_data.weight_unit,
        reps=set_data.reps,
        duration_seconds=set_data.duration_seconds,
        assistance_weight=set_data.assistance_weight,
        assistance_weight_unit=set_data.assistance_weight_unit,
    )

    db.add(exercise_set)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Exercise set already exists",
        )

    db.refresh(exercise_set)

    return exercise_set

@router.patch(
    "/{set_id}",
    response_model=ExerciseSetResponse,
)
def update_exercise_set(
    set_id: int,
    set_data: ExerciseSetUpdate,
    db: Session = Depends(get_db),
):
    # get the existing set
    exercise_set = db.get(ExerciseSet, set_id)

    if exercise_set is None:
        raise HTTPException(
            status_code=404,
            detail="Exercise set not found",
        )

    # get the exercise type
    exercise = db.get(Exercise, exercise_set.exercise_id)

    if exercise is None:
        raise HTTPException(
            status_code=404,
            detail="Exercise not found",
        )

    # track which fields were actually supplied
    fields = set_data.model_fields_set

    # build the proposed final state
    set_number = (
        set_data.set_number
        if "set_number" in fields
        else exercise_set.set_number
    )

    weight = (
        set_data.weight
        if "weight" in fields
        else exercise_set.weight
    )

    weight_unit = (
        set_data.weight_unit
        if "weight_unit" in fields
        else exercise_set.weight_unit
    )

    reps = (
        set_data.reps
        if "reps" in fields
        else exercise_set.reps
    )

    duration_seconds = (
        set_data.duration_seconds
        if "duration_seconds" in fields
        else exercise_set.duration_seconds
    )

    assistance_weight = (
        set_data.assistance_weight
        if "assistance_weight" in fields
        else exercise_set.assistance_weight
    )

    assistance_weight_unit = (
        set_data.assistance_weight_unit
        if "assistance_weight_unit" in fields
        else exercise_set.assistance_weight_unit
    )

    # validate the final state
    try:
        validate_exercise_set_values(
            exercise.exercise_type,
            set_number=set_number,
            weight=weight,
            weight_unit=weight_unit,
            reps=reps,
            duration_seconds=duration_seconds,
            assistance_weight=assistance_weight,
            assistance_weight_unit=assistance_weight_unit,
        )
    except ExerciseSetValidationError as exc:
        raise HTTPException(
            status_code=422,
            detail=str(exc),
        ) from None

    # apply the supplied changes
    if "set_number" in fields:
        exercise_set.set_number = set_data.set_number

    if "weight" in fields:
        exercise_set.weight = set_data.weight

    if "weight_unit" in fields:
        exercise_set.weight_unit = set_data.weight_unit

    if "reps" in fields:
        exercise_set.reps = set_data.reps

    if "duration_seconds" in fields:
        exercise_set.duration_seconds = set_data.duration_seconds

    if "assistance_weight" in fields:
        exercise_set.assistance_weight = set_data.assistance_weight

    if "assistance_weight_unit" in fields:
        exercise_set.assistance_weight_unit = set_data.assistance_weight_unit

    # save changes
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Exercise set already exists",
        )

    db.refresh(exercise_set)

    return exercise_set


@router.delete("/{set_id}")
def delete_exercise_set(
    set_id: int,
    db: Session = Depends(get_db),
):
    exercise_set = db.get(ExerciseSet, set_id)

    if exercise_set is None:
        raise HTTPException(
            status_code=404,
            detail="Exercise set not found",
        )

    session_id = exercise_set.session_id
    exercise_id = exercise_set.exercise_id

    db.delete(exercise_set)
    db.flush()

    remaining_sets = db.scalars(
        select(ExerciseSet)
        .where(
            ExerciseSet.session_id == session_id,
            ExerciseSet.exercise_id == exercise_id,
        )
        .order_by(ExerciseSet.set_number)
    ).all()


    # temporarily move set numbers out of the way
    for index, exercise_set in enumerate(
        remaining_sets,
        start=1,
    ):
        exercise_set.set_number = -index

    db.flush()

    # assign the final sequential numbers
    for index, exercise_set in enumerate(
        remaining_sets,
        start=1,
    ):
        exercise_set.set_number = index

    db.commit()

    return {"message": "Exercise set deleted successfully"}
