from fastapi import FastAPI

from app.api.exercises import router as exercises_router
from app.api.users import router as users_router

app = FastAPI()


app.include_router(
    users_router,
    prefix="/api",
)

app.include_router(
    exercises_router,
    prefix="/api",
)