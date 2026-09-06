from sqlalchemy import select

from app.db.database import SessionLocal
from app.models import Exercise, ExerciseType


EXERCISES = [
    # chest
    {
        "name": "Bench Press",
        "muscle_group": "chest",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Incline Bench Press",
        "muscle_group": "chest",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Dumbbell Bench Press",
        "muscle_group": "chest",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Dumbbell Fly",
        "muscle_group": "chest",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Push Up",
        "muscle_group": "chest",
        "exercise_type": ExerciseType.BODYWEIGHT,
    },

    # back
    {
        "name": "Deadlift",
        "muscle_group": "back",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Barbell Row",
        "muscle_group": "back",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Seated Cable Row",
        "muscle_group": "back",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Lat Pulldown",
        "muscle_group": "back",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Pull Up",
        "muscle_group": "back",
        "exercise_type": ExerciseType.BODYWEIGHT,
    },
    {
        "name": "Assisted Pull Up",
        "muscle_group": "back",
        "exercise_type": ExerciseType.ASSISTED,
    },

    # shoulders
    {
        "name": "Overhead Press",
        "muscle_group": "shoulders",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Dumbbell Shoulder Press",
        "muscle_group": "shoulders",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Lateral Raise",
        "muscle_group": "shoulders",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Face Pull",
        "muscle_group": "shoulders",
        "exercise_type": ExerciseType.WEIGHTED,
    },

    # biceps
    {
        "name": "Barbell Curl",
        "muscle_group": "biceps",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Dumbbell Curl",
        "muscle_group": "biceps",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Hammer Curl",
        "muscle_group": "biceps",
        "exercise_type": ExerciseType.WEIGHTED,
    },

    # triceps
    {
        "name": "Tricep Pushdown",
        "muscle_group": "triceps",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Overhead Tricep Extension",
        "muscle_group": "triceps",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Dips",
        "muscle_group": "triceps",
        "exercise_type": ExerciseType.BODYWEIGHT,
    },
    {
        "name": "Assisted Dips",
        "muscle_group": "triceps",
        "exercise_type": ExerciseType.ASSISTED,
    },

    # legs
    {
        "name": "Squat",
        "muscle_group": "legs",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Front Squat",
        "muscle_group": "legs",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Leg Press",
        "muscle_group": "legs",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Romanian Deadlift",
        "muscle_group": "legs",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Leg Extension",
        "muscle_group": "legs",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Leg Curl",
        "muscle_group": "legs",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Calf Raise",
        "muscle_group": "legs",
        "exercise_type": ExerciseType.WEIGHTED,
    },

    # core
    {
        "name": "Plank",
        "muscle_group": "core",
        "exercise_type": ExerciseType.DURATION,
    },
    {
        "name": "Dead Hang",
        "muscle_group": "back",
        "exercise_type": ExerciseType.DURATION,
    },
    {
        "name": "Hanging Knee Raise",
        "muscle_group": "core",
        "exercise_type": ExerciseType.BODYWEIGHT,
    },
    {
        "name": "Crunch",
        "muscle_group": "core",
        "exercise_type": ExerciseType.BODYWEIGHT,
    },
]


def seed_exercises() -> None:
    db = SessionLocal()

    try:
        added = 0

        for exercise_data in EXERCISES:
            existing = db.scalar(
                select(Exercise).where(
                    Exercise.name.ilike(exercise_data["name"])
                )
            )

            if existing is None:
                db.add(Exercise(**exercise_data))
                added += 1

        db.commit()

        print(f"Added {added} exercises.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_exercises()