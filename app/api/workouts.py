from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models import User, Workout
from app.schemas import WorkoutCreate, WorkoutResponse, WorkoutUpdate

router = APIRouter(prefix="/workouts", tags=["workouts"])

@router.get("/", response_model=list[WorkoutResponse])
def get_workouts(db: Session = Depends(get_db)):
    return db.query(Workout).all()

@router.get("/{workout_id}", response_model=WorkoutResponse)
def get_workout(
    workout_id: int,
    db: Session = Depends(get_db),
):
    workout = db.get(Workout, workout_id)

    if workout is None:
        raise HTTPException(
            status_code=404,
            detail="Workout not found",
        )

    return workout

@router.post("/", response_model=WorkoutResponse)
def create_workout(
    workout_data: WorkoutCreate,
    db: Session = Depends(get_db),
):
    user = db.get(User, workout_data.user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    workout = Workout(
        user_id=workout_data.user_id,
        name=workout_data.name,
    )

    db.add(workout)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Workout with this name already exists",
        )

    db.refresh(workout)

    return workout

@router.put("/{workout_id}", response_model=WorkoutResponse)
def update_workout(
    workout_id: int,
    workout_data: WorkoutUpdate,
    db: Session = Depends(get_db),
):
    workout = db.get(Workout, workout_id)

    if workout is None:
        raise HTTPException(
            status_code=404,
            detail="Workout not found",
        )

    workout.name = workout_data.name

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Workout with this name already exists",
        )

    db.refresh(workout)

    return workout

@router.delete("/{workout_id}")
def delete_workout(
    workout_id: int,
    db: Session = Depends(get_db),
):
    workout = db.get(Workout, workout_id)

    if workout is None:
        raise HTTPException(
            status_code=404,
            detail="Workout not found",
        )

    db.delete(workout)
    db.commit()

    return {"message": "Workout deleted successfully"}
