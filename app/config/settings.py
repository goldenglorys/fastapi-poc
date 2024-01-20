from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MIN_CART_VALUE_TO_AVOID_SURCHARGE: int = Field(
        1000,
        description="Minimum cart value to avoid surcharge",
    )
    MIN_CART_FEE: int = Field(
        0,
        description="Minimum cart fee",
    )

    BASE_DISTANCE_FEE_THRESHOLD: int = Field(
        1000,
        description="Base distance fee threshold",
    )
    BASE_DISTANCE_FEE: int = Field(
        200,
        description="Base distance fee",
    )
    DISTANCE_SURCHARGE: int = Field(
        100,
        description="Distance surcharge",
    )

    BULK_ITEM_FEE: int = Field(
        120,
        description="Bulk item fee",
    )
    ITEM_SURCHARGE: int = Field(
        50,
        description="Item surcharge",
    )
    MAX_ITEMS_WITHOUT_SURCHARGE: int = Field(
        4,
        description="Maximum items without surcharge",
    )
    MIN_ITEM_FEE: int = Field(
        0,
        description="Minimum item fee",
    )

    FRIDAY_DAY_OF_WEEK: int = Field(
        5,
        description="Friday: Day of the week",
    )
    LOWER_THRESHOLD_UTC: int = Field(
        15,
        description="Friday rush: Lower threshold UTC",
    )
    UPPER_THRESHOLD_UTC: int = Field(
        19,
        description="Friday rush: Upper threshold UTC",
    )
    FRIDAY_RUSH_MULTIPLIER: float = Field(
        1.2,
        description="Friday rush: Multiplier",
    )
    MAX_DELIVERY_FEE: int = Field(
        1500,
        description="Maximum delivery fee"
    )

    model_config = SettingsConfigDict(env_file=".env")


SETTINGS = Settings()
