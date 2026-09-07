from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.exercises import router as exercises_router
from app.api.users import router as users_router
from app.api.workouts import router as workouts_router
from app.api.workout_sessions import router as workout_sessions_router
from app.api.exercise_sets import router as exercise_sets_router
from app.api.workout_session_exercies import router as workout_session_exercises_router

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static",
)

templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )


# %% Routers / API
app.include_router(
    users_router,
    prefix="/api",
)

app.include_router(
    exercises_router,
    prefix="/api",
)

app.include_router(
    workouts_router,
    prefix="/api",
)

app.include_router(
    workout_sessions_router,
    prefix="/api"
)

app.include_router(
    exercise_sets_router,
    prefix="/api"
)

app.include_router(
    workout_session_exercises_router,
    prefix="/api"
)