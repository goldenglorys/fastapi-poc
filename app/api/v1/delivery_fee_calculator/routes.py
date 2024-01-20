from fastapi import APIRouter, HTTPException

from .helpers import DeliveryFeeCalculator
from .schemas import (DeliveryFeeCalculatorInputSchema,
                      DeliveryFeeCalculatorOutputSchema)

router = APIRouter(prefix="/delivery-fee-calculator", tags=["Delivery Fee Calculator"])


@router.post(
    "/",
    summary="Calculates the delivery fee based on the information in the request payload (JSON)",
    description="""
        The delivery price depends on the cart value, the number of items in the cart, 
        the time of the order, and the delivery distance.

            :param data: 
                DeliveryFeeCalculatorInputSchema: The JSON request payload

            :return:
                DeliveryFeeCalculatorOutputSchema: The response JSON data 
    """,
)
async def calculate_delivery_fee_endpoint(
    data: DeliveryFeeCalculatorInputSchema,
) -> DeliveryFeeCalculatorOutputSchema:
    try:
        calculator = DeliveryFeeCalculator()
        fee = calculator.calculate_delivery_fee(
            data.cart_value, data.delivery_distance, data.number_of_items, data.time
        )
        return DeliveryFeeCalculatorOutputSchema(delivery_fee=fee)
    except Exception as error:
        raise HTTPException(status_code=400, detail=str(error))
