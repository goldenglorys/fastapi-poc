import pytest
from app.api.v1.delivery_fee_calculator.helpers import DeliveryFeeCalculator
from app.config.settings import SETTINGS

# Mocking a delivery time for testing
mock_delivery_time = "2024-01-19T13:00:00Z"


@pytest.fixture
def calculator():
    return DeliveryFeeCalculator()


@pytest.mark.parametrize(
    "cart_value, expected_cart_fee",
    [(890, 110), (1100, 0)],
)
def test_calculate_cart_fee(calculator, cart_value, expected_cart_fee):
    assert calculator.calculate_cart_fee(cart_value) == expected_cart_fee


@pytest.mark.parametrize(
    "delivery_distance, expected_distance_fee",
    [(999, 200), (1499, 300), (1500, 400), (1501, 400)],
)
def test_calculate_distance_fee(calculator, delivery_distance, expected_distance_fee):
    assert calculator.calculate_distance_fee(delivery_distance) == expected_distance_fee


@pytest.mark.parametrize(
    "number_of_items, expected_item_fee",
    [(4, 0), (5, 50), (10, 300), (13, 570), (14, 620)],
)
def test_calculate_item_fee(calculator, number_of_items, expected_item_fee):
    assert calculator.calculate_item_fee(number_of_items) == expected_item_fee


@pytest.mark.parametrize(
    "base_fee, delivery_time, expected_fee",
    [(1000, "2024-01-19T16:00:00Z", 1200), (1000, "2024-01-16T13:00:00Z", 1000)],
)
def test_apply_friday_rush_multiplier(
    calculator, base_fee, delivery_time, expected_fee
):
    assert (
        calculator.apply_friday_rush_multiplier(base_fee, delivery_time) == expected_fee
    )


@pytest.mark.parametrize(
    "cart_value, delivery_distance, number_of_items, expected_fee",
    [
        (800, 1500, 5, 650),
        (1000, 1500, 5, 450),
        (1000, 1500, 5, 450),
        (800, 2000, 10, 1000),
    ],
)
def test_calculate_delivery_fee(
    calculator, cart_value, delivery_distance, number_of_items, expected_fee
):
    assert (
        calculator.calculate_delivery_fee(
            cart_value, delivery_distance, number_of_items, mock_delivery_time
        )
        == expected_fee
    )


@pytest.mark.parametrize(
    "cart_value, expected_delivery_fee",
    [
        (SETTINGS.FREE_DELIVERY_THRESHOLD, 0),
        (SETTINGS.FREE_DELIVERY_THRESHOLD + 100, 0),
    ],
)
def test_free_delivery_needed(calculator, cart_value, expected_delivery_fee):
    assert (
        calculator.calculate_delivery_fee(cart_value, 1500, 5, mock_delivery_time)
        == expected_delivery_fee
    )
