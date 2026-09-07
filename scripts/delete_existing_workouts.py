from app.db.database import SessionLocal
from app.models import WorkoutSession, WorkoutSessionExercise

db = SessionLocal()

db.query(WorkoutSessionExercise).delete()
db.query(WorkoutSession).delete()

db.commit()
db.close()

exit()
