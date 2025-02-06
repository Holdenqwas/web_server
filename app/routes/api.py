from fastapi import APIRouter

from app.routes import (
    alice, 
    auth, 
    exercise, 
    homeassistant,
    shop_list, 
    training, 
    users, 
)

router = APIRouter()
router.include_router(alice.router, prefix="/alice", tags=["Alice"])
router.include_router(auth.router, tags=["Auth"])
router.include_router(exercise.router, prefix="/exercise", tags=["Exercise"])
router.include_router(homeassistant.router, prefix="/homeassistant", tags=["Home Assistant"])
router.include_router(shop_list.router, prefix="/shop_list", tags=["Shop list"])
router.include_router(training.router, prefix="/training", tags=["Training"])
router.include_router(users.router, prefix="/users", tags=["Users"])
