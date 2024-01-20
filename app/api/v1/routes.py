from fastapi import APIRouter

router = APIRouter(prefix="/api/v1", tags=["API v1"])


@router.get("/")
def index() -> dict[str, str]:
    """Endpoint for the root URL of the v1 API.

    Returns:
        dict[str, str]: A dictionary containing the welcome message.
    """
    return {"message": "Welcome to the v1 of the Delivery Fee Calculator Server"}

