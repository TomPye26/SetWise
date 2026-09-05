from fastapi import FastAPI

from app.api.exercises import router as exercises_router

app = FastAPI()

app.include_router(
    exercises_router,
    prefix="/api",
)
