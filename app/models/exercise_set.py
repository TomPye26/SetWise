from decimal import Decimal
from enum import Enum

from sqlalchemy import Enum as SQLEnum, ForeignKey, Numeric, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class WeightUnit(str, Enum):
    KG = "kg"
    LB = "lb"


class ExerciseSet(Base):
    __tablename__ = "exercise_sets"

    __table_args__ = (
        UniqueConstraint(
            "session_id",
            "exercise_id",
            "set_number",
            name="uq_exercise_set_number",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)

    session_id: Mapped[int] = mapped_column(
        ForeignKey("workout_sessions.id"),
        nullable=False,
    )

    exercise_id: Mapped[int] = mapped_column(
        ForeignKey("exercises.id"),
        nullable=False,
    )

    set_number: Mapped[int] = mapped_column(nullable=False)

    weight: Mapped[Decimal | None] = mapped_column(
        Numeric(7, 2),
        nullable=True,
    )

    weight_unit: Mapped[WeightUnit | None] = mapped_column(
        SQLEnum(
            WeightUnit,
            values_callable=lambda enum: [item.value for item in enum],
        ),
        nullable=True,
    )

    reps: Mapped[int | None] = mapped_column(nullable=True)

    duration_seconds: Mapped[int | None] = mapped_column(nullable=True)

    assistance_weight: Mapped[Decimal | None] = mapped_column(
        Numeric(7, 2),
        nullable=True,
    )

    assistance_weight_unit: Mapped[WeightUnit | None] = mapped_column(
        SQLEnum(
            WeightUnit,
            values_callable=lambda enum: [item.value for item in enum],
        ),
        nullable=True,
    )
