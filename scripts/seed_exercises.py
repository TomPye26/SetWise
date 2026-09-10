from sqlalchemy import select

from app.db.database import SessionLocal
from app.models import Exercise, ExerciseType


EXERCISES = [
    # Chest
    {
        "name": "Bench Press",
        "muscle_group": "Chest",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Incline Bench Press",
        "muscle_group": "Chest",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Decline Bench Press",
        "muscle_group": "Chest",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Dumbbell Bench Press",
        "muscle_group": "Chest",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Incline Dumbbell Bench Press",
        "muscle_group": "Chest",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Decline Dumbbell Bench Press",
        "muscle_group": "Chest",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Machine Chest Press",
        "muscle_group": "Chest",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Cable Chest Press",
        "muscle_group": "Chest",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Dumbbell Fly",
        "muscle_group": "Chest",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Cable Fly",
        "muscle_group": "Chest",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Pec Deck",
        "muscle_group": "Chest",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Push Up",
        "muscle_group": "Chest",
        "exercise_type": ExerciseType.BODYWEIGHT,
    },
    {
        "name": "Decline Push Up",
        "muscle_group": "Chest",
        "exercise_type": ExerciseType.BODYWEIGHT,
    },
    {
        "name": "Chest Dip",
        "muscle_group": "Chest",
        "exercise_type": ExerciseType.BODYWEIGHT,
    },

    # Back
    {
        "name": "Deadlift",
        "muscle_group": "Back",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Sumo Deadlift",
        "muscle_group": "Back",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Barbell Row",
        "muscle_group": "Back",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Pendlay Row",
        "muscle_group": "Back",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Dumbbell Row",
        "muscle_group": "Back",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Chest Supported Dumbbell Row",
        "muscle_group": "Back",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Machine Row",
        "muscle_group": "Back",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Seated Cable Row",
        "muscle_group": "Back",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Single Arm Cable Row",
        "muscle_group": "Back",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Lat Pulldown",
        "muscle_group": "Back",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Close Grip Lat Pulldown",
        "muscle_group": "Back",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Straight Arm Pulldown",
        "muscle_group": "Back",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Pull Up",
        "muscle_group": "Back",
        "exercise_type": ExerciseType.BODYWEIGHT,
    },
    {
        "name": "Chin Up",
        "muscle_group": "Back",
        "exercise_type": ExerciseType.BODYWEIGHT,
    },
    {
        "name": "Assisted Pull Up",
        "muscle_group": "Back",
        "exercise_type": ExerciseType.ASSISTED,
    },
    {
        "name": "Assisted Chin Up",
        "muscle_group": "Back",
        "exercise_type": ExerciseType.ASSISTED,
    },

    # Shoulders
    {
        "name": "Overhead Press",
        "muscle_group": "Shoulders",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Dumbbell Shoulder Press",
        "muscle_group": "Shoulders",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Arnold Press",
        "muscle_group": "Shoulders",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Machine Shoulder Press",
        "muscle_group": "Shoulders",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Dumbbell Lateral Raise",
        "muscle_group": "Shoulders",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Cable Lateral Raise",
        "muscle_group": "Shoulders",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Machine Lateral Raise",
        "muscle_group": "Shoulders",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Front Raise",
        "muscle_group": "Shoulders",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Reverse Fly",
        "muscle_group": "Shoulders",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Cable Reverse Fly",
        "muscle_group": "Shoulders",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Face Pull",
        "muscle_group": "Shoulders",
        "exercise_type": ExerciseType.WEIGHTED,
    },

    # Biceps
    {
        "name": "Barbell Curl",
        "muscle_group": "Biceps",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "EZ Bar Curl",
        "muscle_group": "Biceps",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Dumbbell Curl",
        "muscle_group": "Biceps",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Hammer Curl",
        "muscle_group": "Biceps",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Incline Dumbbell Curl",
        "muscle_group": "Biceps",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Preacher Curl",
        "muscle_group": "Biceps",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Machine Preacher Curl",
        "muscle_group": "Biceps",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Cable Curl",
        "muscle_group": "Biceps",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Bayesian Curl",
        "muscle_group": "Biceps",
        "exercise_type": ExerciseType.WEIGHTED,
    },

    # Triceps
    {
        "name": "Tricep Pushdown",
        "muscle_group": "Triceps",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Rope Tricep Pushdown",
        "muscle_group": "Triceps",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Overhead Tricep Extension",
        "muscle_group": "Triceps",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Dumbbell Overhead Tricep Extension",
        "muscle_group": "Triceps",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Cable Overhead Tricep Extension",
        "muscle_group": "Triceps",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Skull Crusher",
        "muscle_group": "Triceps",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Dumbbell Skull Crusher",
        "muscle_group": "Triceps",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Close Grip Bench Press",
        "muscle_group": "Triceps",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Tricep Dip",
        "muscle_group": "Triceps",
        "exercise_type": ExerciseType.BODYWEIGHT,
    },
    {
        "name": "Assisted Tricep Dip",
        "muscle_group": "Triceps",
        "exercise_type": ExerciseType.ASSISTED,
    },

    # Legs
    {
        "name": "Back Squat",
        "muscle_group": "Legs",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Front Squat",
        "muscle_group": "Legs",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Goblet Squat",
        "muscle_group": "Legs",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Hack Squat",
        "muscle_group": "Legs",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Leg Press",
        "muscle_group": "Legs",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Romanian Deadlift",
        "muscle_group": "Legs",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Dumbbell Romanian Deadlift",
        "muscle_group": "Legs",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Hip Thrust",
        "muscle_group": "Legs",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Barbell Hip Thrust",
        "muscle_group": "Legs",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Bulgarian Split Squat",
        "muscle_group": "Legs",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Walking Lunge",
        "muscle_group": "Legs",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Reverse Lunge",
        "muscle_group": "Legs",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Leg Extension",
        "muscle_group": "Legs",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Seated Leg Curl",
        "muscle_group": "Legs",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Lying Leg Curl",
        "muscle_group": "Legs",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Standing Calf Raise",
        "muscle_group": "Legs",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Seated Calf Raise",
        "muscle_group": "Legs",
        "exercise_type": ExerciseType.WEIGHTED,
    },

    # Core
    {
        "name": "Plank",
        "muscle_group": "Core",
        "exercise_type": ExerciseType.DURATION,
    },
    {
        "name": "Side Plank",
        "muscle_group": "Core",
        "exercise_type": ExerciseType.DURATION,
    },
    {
        "name": "Dead Bug",
        "muscle_group": "Core",
        "exercise_type": ExerciseType.BODYWEIGHT,
    },
    {
        "name": "Crunch",
        "muscle_group": "Core",
        "exercise_type": ExerciseType.BODYWEIGHT,
    },
    {
        "name": "Cable Crunch",
        "muscle_group": "Core",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Hanging Knee Raise",
        "muscle_group": "Core",
        "exercise_type": ExerciseType.BODYWEIGHT,
    },
    {
        "name": "Hanging Leg Raise",
        "muscle_group": "Core",
        "exercise_type": ExerciseType.BODYWEIGHT,
    },
    {
        "name": "Ab Wheel Rollout",
        "muscle_group": "Core",
        "exercise_type": ExerciseType.BODYWEIGHT,
    },
    {
        "name": "Russian Twist",
        "muscle_group": "Core",
        "exercise_type": ExerciseType.WEIGHTED,
    },

    # Forearms / Grip
    {
        "name": "Wrist Curl",
        "muscle_group": "Forearms",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Reverse Wrist Curl",
        "muscle_group": "Forearms",
        "exercise_type": ExerciseType.WEIGHTED,
    },
    {
        "name": "Farmer's Walk",
        "muscle_group": "Forearms",
        "exercise_type": ExerciseType.DURATION,
    },
    {
        "name": "Dead Hang",
        "muscle_group": "Forearms",
        "exercise_type": ExerciseType.DURATION,
    },
]


def seed_exercises() -> None:
    db = SessionLocal()

    try:
        added = 0
        updated = 0

        for exercise_data in EXERCISES:
            existing = db.scalar(
                select(Exercise).where(
                    Exercise.name.ilike(exercise_data["name"])
                )
            )

            if existing is None:
                db.add(Exercise(**exercise_data))
                added += 1
            else:
                existing.name = exercise_data["name"]
                existing.muscle_group = exercise_data["muscle_group"]
                existing.exercise_type = exercise_data["exercise_type"]
                updated += 1

        db.commit()

        print(
            f"Added {added} exercises, "
            f"updated {updated} exercises."
        )

    finally:
        db.close()

if __name__ == "__main__":
    seed_exercises()