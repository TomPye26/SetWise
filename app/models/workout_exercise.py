from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class WorkoutExercise(Base):
    __tablename__ = "workout_exercises"

    workout_id: Mapped[int] = mapped_column(
        ForeignKey("workouts.id"),
        primary_key=True,
    )

    exercise_id: Mapped[int] = mapped_column(
        ForeignKey("exercises.id"),
        primary_key=True,
    )

    position: Mapped[int] = mapped_column(nullable=False)
