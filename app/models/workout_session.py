from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class WorkoutSession(Base):
    __tablename__ = "workout_sessions"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    workout_id: Mapped[int] = mapped_column(
        ForeignKey("workouts.id"),
        nullable=False,
    )

    started_at: Mapped[datetime] = mapped_column(nullable=False)

    completed_at: Mapped[datetime | None] = mapped_column(nullable=True)
