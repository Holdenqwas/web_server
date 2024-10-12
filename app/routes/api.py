from fastapi import APIRouter
from app.routes import training, auth, users, exercise, shop_list

router = APIRouter()
router.include_router(auth.router, tags=["Auth"])
router.include_router(exercise.router, prefix="/exercise", tags=["Exercise"])
router.include_router(shop_list.router, prefix="/shop_list", tags=["Shop list"])
router.include_router(training.router, prefix="/training", tags=["Training"])
router.include_router(users.router, prefix="/users", tags=["Users"])
