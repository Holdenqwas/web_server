from fastapi import APIRouter
from app.routes import training, auth, users, exercise

router = APIRouter()
router.include_router(training.router, prefix="/training", tags=["Training"])
router.include_router(exercise.router, prefix="/exercise", tags=["Exercise"])
router.include_router(users.router, prefix="/users", tags=["Users"])
router.include_router(auth.router, tags=["Auth"])
