from datetime import datetime

from app.config.settings import SETTINGS


class DeliveryFeeCalculator:
    """
    A class responsible for calculating delivery fees based on specified rules and parameters.

    Rules:
    - Cart fee is calculated based on cart value.
    - Distance fee is calculated based on delivery distance.
    - Item fee is calculated based on the number of items in the cart.
    - Friday rush multiplier is applied during specific hours.

    Attributes:
    - settings: An instance of the SETTINGS class containing fee calculation parameters.
    """

    def __init__(self):
        """
        Initialize the DeliveryFeeCalculator with the provided settings.

        The settings contain constant parameters such as minimum cart value, distance fees, item fees, and Friday rush details.
        """
        self.settings = SETTINGS

    def calculate_cart_fee(self, cart_value: int) -> int:
        """
        Calculate the cart fee based on the provided cart value.

        Rules:
        - If the cart value is less than 10€, a small order surcharge is added.
        - The surcharge is the difference between the cart value and 10€.

        :param cart_value: The value of the items in the cart in cents.
        :return: The calculated cart fee in cents.
        """
        return max(
            self.settings.MIN_CART_VALUE_TO_AVOID_SURCHARGE - cart_value,
            self.settings.MIN_CART_FEE,
        )

    def calculate_distance_fee(self, delivery_distance: int) -> int:
        """
        Calculate the distance fee based on the provided delivery distance.

        Rules:
        - A delivery fee of 2€ is applied for the first 1000 meters.
        - For distances longer than 1000 meters, 1€ is added for every additional 500 meters.

        :param delivery_distance: The delivery distance in meters.
        :return: The calculated distance fee in cents.
        """
        if delivery_distance % 500 == 0:
            distance_fee_mod_500 = (
                delivery_distance // 500
            ) * self.settings.DISTANCE_SURCHARGE
            return distance_fee_mod_500
        else:
            quotient, remainder = divmod(delivery_distance, 500)
            rounded_distance = (delivery_distance + 500) - remainder
            distance_fee_rounded = (
                rounded_distance // 500
            ) * self.settings.DISTANCE_SURCHARGE
            return distance_fee_rounded

    def calculate_item_fee(self, number_of_items: int) -> int:
        """
        Calculate the item fee based on the provided number of items.

        Rules:
        - If the number of items is five or more, a 50 cent surcharge is added for each item above and including the fifth item.
        - An extra "bulk" fee of 1.20€ applies for more than 12 items.

        :param number_of_items: The number of items in the cart.
        :return: The calculated item fee in cents.
        """
        if 5 <= number_of_items <= 12:
            return (
                number_of_items - self.settings.MAX_ITEMS_WITHOUT_SURCHARGE
            ) * self.settings.ITEM_SURCHARGE
        elif number_of_items > 12:
            return (
                number_of_items - self.settings.MAX_ITEMS_WITHOUT_SURCHARGE
            ) * self.settings.ITEM_SURCHARGE + self.settings.BULK_ITEM_FEE
        else:
            return self.settings.MIN_ITEM_FEE

    def apply_friday_rush_multiplier(self, base_fee: int, delivery_time: str) -> int:
        """
        Apply the Friday rush multiplier to the base fee during the specified time.

        Rules:
        - During the Friday rush (3 - 7 PM UTC), the delivery fee is multiplied by 1.2x.
        - The fee cannot exceed the maximum of 15€.

        :param base_fee: The base delivery fee in cents.
        :param delivery_time: The delivery time in ISO format.
        :return: The final delivery fee after applying the Friday rush rules in cents.
        """
        date_time = datetime.strptime(delivery_time, "%Y-%m-%dT%H:%M:%SZ")
        day_of_week, utc_hour = date_time.isoweekday(), date_time.hour

        if (
            day_of_week == self.settings.FRIDAY_DAY_OF_WEEK
            and self.settings.LOWER_THRESHOLD_UTC
            <= utc_hour
            <= self.settings.UPPER_THRESHOLD_UTC
        ):
            return min(
                base_fee * self.settings.FRIDAY_RUSH_MULTIPLIER,
                self.settings.MAX_DELIVERY_FEE,
            )
        else:
            return min(base_fee, self.settings.MAX_DELIVERY_FEE)

    def calculate_delivery_fee(
        self,
        cart_value: int,
        delivery_distance: int,
        number_of_items: int,
        delivery_time: str,
    ) -> int:
        """
        Calculate the total delivery fee based on cart value, delivery distance, items, and delivery time.

        :param cart_value: The value of the items in the cart in cents.
        :param delivery_distance: The delivery distance in meters.
        :param number_of_items: The number of items in the cart.
        :param delivery_time: The delivery time in ISO format.
        :return: The final calculated delivery fee in cents.
        """
        if cart_value >= self.settings.FREE_DELIVERY_THRESHOLD:
            return 0
        cart_fee = self.calculate_cart_fee(cart_value)
        distance_fee = self.calculate_distance_fee(delivery_distance)
        item_fee = self.calculate_item_fee(number_of_items)
        total_fee = cart_fee + distance_fee + item_fee
        final_fee = self.apply_friday_rush_multiplier(total_fee, delivery_time)
        return final_fee
