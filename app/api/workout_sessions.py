from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models import User, Workout, WorkoutSession
from app.schemas import (
    WorkoutSessionCreate,
    WorkoutSessionResponse,
    WorkoutSessionUpdate,
)

router = APIRouter(
    prefix="/workout-sessions",
    tags=["workout-sessions"],
)


@router.get("/", response_model=list[WorkoutSessionResponse])
def get_workout_sessions(
    db: Session = Depends(get_db),
):
    return db.query(WorkoutSession).all()


@router.get("/{session_id}", response_model=WorkoutSessionResponse)
def get_workout_session(
    session_id: int,
    db: Session = Depends(get_db),
):
    session = db.get(WorkoutSession, session_id)

    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Workout session not found",
        )

    return session

@router.post("/", response_model=WorkoutSessionResponse, status_code=201)
def create_workout_session(
    session_data: WorkoutSessionCreate,
    db: Session = Depends(get_db),
):
    user = db.get(User, session_data.user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    if session_data.workout_id is not None:
        workout = db.get(Workout, session_data.workout_id)

        if workout is None:
            raise HTTPException(
                status_code=404,
                detail="Workout not found",
            )

    if session_data.completed_at is None:
        active_session = db.scalar(
            select(WorkoutSession).where(
                WorkoutSession.user_id == session_data.user_id,
                WorkoutSession.completed_at.is_(None),
            )
        )

        if active_session is not None:
            raise HTTPException(
                status_code=409,
                detail="User already has an active workout session",
            )

    started_at = session_data.started_at or datetime.utcnow()

    session = WorkoutSession(
        user_id=session_data.user_id,
        workout_id=session_data.workout_id,
        label=session_data.label,
        started_at=started_at,
        completed_at=session_data.completed_at,
    )

    db.add(session)
    db.commit()
    db.refresh(session)

    return session


@router.patch("/{session_id}", response_model=WorkoutSessionResponse)
def update_workout_session(
    session_id: int,
    session_data: WorkoutSessionUpdate,
    db: Session = Depends(get_db),
):
    session = db.get(WorkoutSession, session_id)

    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Workout session not found",
        )

    session.completed_at = session_data.completed_at

    db.commit()
    db.refresh(session)

    return session


@router.delete("/{session_id}")
def delete_workout_session(
    session_id: int,
    db: Session = Depends(get_db),
):
    session = db.get(WorkoutSession, session_id)

    if session is None:
        raise HTTPException(
            status_code=404,
            detail="Workout session not found",
        )

    db.delete(session)
    db.commit()

    return {"message": "Workout session deleted successfully"}


@router.get(
    "/user/{user_id}/active",
    response_model=WorkoutSessionResponse,
)
def get_active_workout_session(
    user_id: int,
    db: Session = Depends(get_db),
):
    session = db.scalar(
        select(WorkoutSession)
        .where(
            WorkoutSession.user_id == user_id,
            WorkoutSession.completed_at.is_(None),
        )
    )

    if session is None:
        raise HTTPException(
            status_code=404,
            detail="No active workout found",
        )

    return session

@router.get(
    "/user/{user_id}",
    response_model=list[WorkoutSessionResponse],
)
def get_user_workout_sessions(
    user_id: int,
    db: Session = Depends(get_db),
):
    user = db.get(User, user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    all_workout_sessions = db.scalars(
        select(WorkoutSession)
        .where(WorkoutSession.user_id == user_id)
        .order_by(WorkoutSession.started_at.desc())
    ).all()

    return all_workout_sessions
