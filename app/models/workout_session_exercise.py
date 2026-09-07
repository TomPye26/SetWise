from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class WorkoutSessionExercise(Base):
    __tablename__ = "workout_session_exercises"

    session_id: Mapped[int] = mapped_column(
        ForeignKey("workout_sessions.id"),
        primary_key=True,
    )

    exercise_id: Mapped[int] = mapped_column(
        ForeignKey("exercises.id"),
        primary_key=True,
    )

    position: Mapped[int] = mapped_column(
        nullable=False,
    )
