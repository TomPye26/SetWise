from fastapi import FastAPI

from app.api.exercises import router as exercises_router
from app.db.database import Base, engine
from app.models import Exercise

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    exercises_router,
    prefix="/api",
)
