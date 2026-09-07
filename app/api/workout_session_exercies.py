from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models import Exercise, WorkoutSession, WorkoutSessionExercise
from app.schemas.workout_session_exercise import (
    WorkoutSessionExerciseCreate,
    WorkoutSessionExerciseResponse,
)

router = APIRouter(
    prefix="/workout-session-exercises",
    tags=["workout-session-exercises"],
)


@router.get(
    "/session/{session_id}",
    response_model=list[WorkoutSessionExerciseResponse],
)
def get_session_exercises(
    session_id: int,
    db: Session = Depends(get_db),
):
    session = db.get(WorkoutSession, session_id)

    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Workout session not found",
        )

    return db.scalars(
        select(WorkoutSessionExercise)
        .where(
            WorkoutSessionExercise.session_id == session_id,
        )
        .order_by(WorkoutSessionExercise.position)
    ).all()


@router.post(
    "/session/{session_id}",
    response_model=WorkoutSessionExerciseResponse,
    status_code=201,
)
def add_session_exercise(
    session_id: int,
    exercise_data: WorkoutSessionExerciseCreate,
    db: Session = Depends(get_db),
):
    session = db.get(WorkoutSession, session_id)

    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Workout session not found",
        )

    exercise = db.get(Exercise, exercise_data.exercise_id)

    if exercise is None:
        raise HTTPException(
            status_code=404,
            detail="Exercise not found",
        )

    existing = db.get(
        WorkoutSessionExercise,
        (session_id, exercise_data.exercise_id),
    )

    if existing is not None:
        raise HTTPException(
            status_code=409,
            detail="Exercise already added to this workout session",
        )

    session_exercise = WorkoutSessionExercise(
        session_id=session_id,
        exercise_id=exercise_data.exercise_id,
        position=exercise_data.position,
    )

    db.add(session_exercise)
    db.commit()
    db.refresh(session_exercise)

    return session_exercise


@router.delete(
    "/session/{session_id}/{exercise_id}",
    status_code=204,
)
def remove_session_exercise(
    session_id: int,
    exercise_id: int,
    db: Session = Depends(get_db),
):
    session_exercise = db.get(
        WorkoutSessionExercise,
        (session_id, exercise_id),
    )

    if session_exercise is None:
        raise HTTPException(
            status_code=404,
            detail="Exercise not found in workout session",
        )

    db.delete(session_exercise)
    db.commit()
