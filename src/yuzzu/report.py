from pathlib import Path

import matplotlib.pyplot as plt

from yuzzu.bond import Bond
from yuzzu.curve import YieldCurve


def analyze_bond(maturity, face_value, coupon_rate, curve_path=None):
    """Compute the main analytics for one bond.

    Args:
        maturity (int): Number of years until maturity.
        face_value (float): Amount repaid at maturity.
        coupon_rate (float): Yearly coupon rate as a decimal.
        curve_path (str | Path): Path to the CSV file used for the yield
            curve.

    Returns:
        dict[str, float | list[float]]: Yield, price, duration, and cash
        flows.
    """
    bond = Bond(maturity, face_value, coupon_rate)
    curve = YieldCurve(curve_path)
    rate = curve.rate(maturity)
    result = {}
    result["yield"] = rate
    result["price"] = bond.price(rate)
    result["duration"] = bond.duration(rate)
    result["cash_flows"] = bond.cash_flows
    return result


def plot_cash_flows(cash_flows, output_path):
    """Save a bar chart of the bond cash flows.

    Args:
        cash_flows (list[float]): List of yearly cash flows.
        output_path (str | Path): Path of the image file to create.

    Returns:
        Path: Output path of the created image.
    """
    output = Path(output_path)
    years = list(range(1, len(cash_flows) + 1))

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar([str(year) for year in years], cash_flows, color="#2f6db2")
    ax.set_title("Bond Cash Flows")
    ax.set_xlabel("Year")
    ax.set_ylabel("Amount")
    ax.grid(axis="y", alpha=0.2)
    fig.tight_layout()
    fig.savefig(output)
    plt.close(fig)

    return output
