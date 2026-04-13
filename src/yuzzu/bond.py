import numpy as np


class Bond:
    """Represent a simple fixed-rate bond with annual coupons."""

    def __init__(self, maturity, face_value, coupon_rate):
        """Create a bond from maturity, face value, and coupon rate.

        Args:
            maturity (int): Number of years until the bond matures.
            face_value (float): Amount repaid at maturity.
            coupon_rate (float): Yearly coupon rate as a decimal.
        """
        if maturity <= 0:
            raise ValueError("maturity must be greater than 0")
        if face_value <= 0:
            raise ValueError("face_value must be greater than 0")
        if coupon_rate < 0:
            raise ValueError("coupon_rate must be non-negative")

        self.maturity = maturity
        self.face_value = face_value
        self.coupon_rate = coupon_rate
        self.cash_flows = self.build_cash_flows()

    def build_cash_flows(self):
        """Build the yearly cash flows of the bond.

        Returns:
            list[float]: Yearly cash flows, with principal added in the last year.
        """
        cash_flows = [self.face_value * self.coupon_rate] * self.maturity
        cash_flows[-1] = cash_flows[-1] + self.face_value
        return cash_flows

    def price(self, rate):
        """Compute the bond price for a given yield.

        Args:
            rate (float): Yield used to discount the cash flows.

        Returns:
            float: Present value of the bond.
        """
        years = np.arange(1, self.maturity + 1, dtype=float)
        cash_flows = np.array(self.cash_flows, dtype=float)
        discount_factors = np.power(1.0 + rate, years)
        return float((cash_flows / discount_factors).sum())

    def duration(self, rate):
        """Compute the Macaulay duration for a given yield.

        Args:
            rate (float): Yield used to discount the cash flows.

        Returns:
            float: Macaulay duration in years.
        """
        years = np.arange(1, self.maturity + 1, dtype=float)
        cash_flows = np.array(self.cash_flows, dtype=float)
        discounted = cash_flows / np.power(1.0 + rate, years)
        weighted_sum = np.dot(years, discounted)
        return float(weighted_sum / discounted.sum())
