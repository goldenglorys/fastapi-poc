from pydantic import BaseModel


class BaseAPISchema(BaseModel):
    """Base class for API schemas.

    Attributes:
        Config (class): Configuration options for the schema.

            - populate_by_name (bool): Whether to allow population by field name.
    """

    class Config:
        """Configuration options for the schema.

        Attributes:
            populate_by_name (bool): Whether to allow population by field name.
        """

        populate_by_name = True