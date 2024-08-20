from fastapi import APIRouter
from app.routes import training, auth

router = APIRouter()
router.include_router(training.router, prefix="/training", tags=["Training"])
router.include_router(auth.router, tags=["Auth"])