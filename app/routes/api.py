from fastapi import APIRouter
from app.routes import training

router = APIRouter()
router.include_router(training.router, prefix="/training", tags=["Training"])