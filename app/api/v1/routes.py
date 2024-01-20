from fastapi import APIRouter

from .delivery_fee_calculator.routes import \
    router as delivery_fee_calculator_router

router = APIRouter(prefix="/api/v1")

router.include_router(router=delivery_fee_calculator_router)
                           