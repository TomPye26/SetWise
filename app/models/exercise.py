from enum import Enum

from sqlalchemy import String
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base

class ExerciseType(str, Enum):
    WEIGHTED = "weighted"
    BODYWEIGHT = "bodyweight"
    ASSISTED = "assisted"
    DURATION = "duration"

class Exercise(Base):
    __tablename__ = "exercises"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    muscle_group: Mapped[str] = mapped_column(String(50))
    exercise_type: Mapped[ExerciseType] = mapped_column(
        SQLEnum(ExerciseType)
    )
