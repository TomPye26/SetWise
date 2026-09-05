from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models import Exercise
from app.schemas import ExerciseCreate, ExerciseResponse, ExerciseUpdate

router = APIRouter(prefix="/exercises", tags=["exercises"])


@router.get("/", response_model=list[ExerciseResponse])
def get_exercises(db: Session = Depends(get_db)):
    return db.query(Exercise).all()


@router.get("/{exercise_id}", response_model=ExerciseResponse)
def get_exercise(exercise_id: int, db: Session = Depends(get_db)):
    exercise = db.get(Exercise, exercise_id)

    if exercise is None:
        raise HTTPException(
            status_code=404,
            detail="Exercise not found",
        )

    return exercise


@router.post("/", response_model=ExerciseResponse)
def create_exercise(
    exercise_data: ExerciseCreate,
    db: Session = Depends(get_db),
):

    exercise = Exercise(
        name=exercise_data.name,
        muscle_group=exercise_data.muscle_group,
        exercise_type=exercise_data.exercise_type,
    )

    db.add(exercise)
    db.commit()
    db.refresh(exercise)

    return exercise


@router.put("/{exercise_id}", response_model=ExerciseResponse)
def update_exercise(
    exercise_id: int,
    exercise_data: ExerciseUpdate,
    db: Session = Depends(get_db),
):
    exercise = db.get(Exercise, exercise_id)

    if exercise is None:
        raise HTTPException(
            status_code=404,
            detail="Exercise not found",
        )

    exercise.name = exercise_data.name
    exercise.muscle_group = exercise_data.muscle_group
    exercise.exercise_type = exercise_data.exercise_type

    db.commit()
    db.refresh(exercise)

    return exercise


@router.delete("/{exercise_id}")
def delete_exercise(
    exercise_id: int,
    db: Session = Depends(get_db),
):
    exercise = db.get(Exercise, exercise_id)

    if exercise is None:
        raise HTTPException(
            status_code=404,
            detail="Exercise not found",
        )

    db.delete(exercise)
    db.commit()

    return {"message": f"Exercise [{exercise.id=}] deleted successfully"}