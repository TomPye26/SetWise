""" Temporary script before a cascade delete is implemented. """

from app.db.database import SessionLocal
from app.models import WorkoutSession, WorkoutSessionExercise, ExerciseSet

db = SessionLocal()

db.query(WorkoutSessionExercise).delete()
db.query(WorkoutSession).delete()
db.query(ExerciseSet).delete()

db.commit()
db.close()

exit()
