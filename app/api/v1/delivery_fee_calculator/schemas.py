from datetime import datetime

from app.api.schemas import BaseAPISchema
from pydantic import Field


class DeliveryFeeCalculatorInputSchema(BaseAPISchema):
    cart_value: int = Field(
        ..., description="Value of the shopping cart in cents.", example=790
    )
    delivery_distance: int = Field(
        ...,
        description="The distance between the store and customer’s location in meters.",
        example=2235,
    )
    number_of_items: int = Field(
        ...,
        description="The number of items in the customer's shopping cart.",
        example=4,
    )
    time: str | datetime = Field(
        ...,
        description="Order time in UTC in ISO format.",
        example="2024-01-15T13:00:00Z",
    )


class  DeliveryFeeCalculatorOutputSchema(BaseAPISchema):
    delivery_fee: int = Field(
        ...,
        description="Calculated delivery fee in cents.",
        example=710,
    )
