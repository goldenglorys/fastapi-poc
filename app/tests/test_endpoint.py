import pytest
from app.api.v1.delivery_fee_calculator.helpers import DeliveryFeeCalculator
from fastapi import HTTPException, status
from fastapi.testclient import TestClient

# Mocking a delivery time for testing
mock_delivery_time = "2024-01-19T13:00:00Z"


@pytest.fixture
def calculator():
    return DeliveryFeeCalculator()


@pytest.fixture
def client():
    from app.main import app

    return TestClient(app)


@pytest.mark.parametrize(
    "cart_value, delivery_distance, number_of_items, time, expected_fee",
    [
        (800, 1500, 5, mock_delivery_time, 550),
        (1000, 1500, 5, mock_delivery_time, 350),
        (790, 2235, 4, mock_delivery_time, 710),
        (800, 2000, 10, mock_delivery_time, 900),
    ],
)
def test_calculate_delivery_fee_endpoint(
    calculator,
    client,
    cart_value,
    delivery_distance,
    number_of_items,
    time,
    expected_fee,
) -> None:
    valid_payload = {
        "cart_value": cart_value,
        "delivery_distance": delivery_distance,
        "number_of_items": number_of_items,
        "time": time,
    }
    response = client.post("/api/v1/delivery-fee-calculator/", json=valid_payload)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"delivery_fee": expected_fee}


@pytest.mark.parametrize(
    "cart_value, delivery_distance, number_of_items, time",
    [
        (None, 1500, 5, mock_delivery_time),  # Missing cart_value
        (800, None, 5, mock_delivery_time),  # Missing delivery_distance
        (800, 1500, None, mock_delivery_time),  # Missing number_of_items
        (800, 1500, 5, None),  # Missing time
        ("invalid", 1500, 5, mock_delivery_time),  # Invalid cart_value
        (800, "invalid", 5, mock_delivery_time),  # Invalid delivery_distance
        (800, 1500, "invalid", mock_delivery_time),  # Invalid number_of_items
    ],
)
def test_calculate_delivery_fee_bad_input(
    client, cart_value, delivery_distance, number_of_items, time
) -> None:
    invalid_payload = {
        "cart_value": cart_value,
        "delivery_distance": delivery_distance,
        "number_of_items": number_of_items,
        "time": time,
    }
    response = client.post("/api/v1/delivery-fee-calculator/", json=invalid_payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.parametrize(
    "cart_value, delivery_distance, number_of_items, time",
    [
        (800, 1500, 5, "invalid"),  # Invalid time
    ],
)
def test_calculate_delivery_fee_bad_time_input(
    client, cart_value, delivery_distance, number_of_items, time
) -> None:
    invalid_payload = {
        "cart_value": cart_value,
        "delivery_distance": delivery_distance,
        "number_of_items": number_of_items,
        "time": time,
    }
    response = client.post("/api/v1/delivery-fee-calculator/", json=invalid_payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_calculate_delivery_fee_exception_handling(client, monkeypatch) -> None:
    def mock_calculate_delivery_fee(*args, **kwargs):
        raise ValueError("Mocked exception")

    monkeypatch.setattr(
        "app.api.v1.delivery_fee_calculator.helpers.DeliveryFeeCalculator.calculate_delivery_fee",
        mock_calculate_delivery_fee,
    )

    valid_payload = {
        "cart_value": 800,
        "delivery_distance": 1500,
        "number_of_items": 5,
        "time": mock_delivery_time,
    }
    response = client.post("/api/v1/delivery-fee-calculator/", json=valid_payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"detail": "Mocked exception"}
