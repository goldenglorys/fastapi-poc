# from app.main import app
# from fastapi import status
# from fastapi.testclient import TestClient

# client = TestClient(app)


# def test_calculate_delivery_fee_endpoint() -> None:
#     """Tests that all characters are converted to upper case."""
#     valid_payload = {
#         "cart_value": 790,
#         "delivery_distance": 2235,
#         "number_of_items": 4,
#         "time": "2024-01-15T13:00:00Z",
#     }
#     response = client.post(
#         "/api/v1/delivery-fee-calculator/",
#         json=valid_payload,
#     )
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json() == {"delivery_fee": 710}

