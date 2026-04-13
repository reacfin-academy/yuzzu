from pathlib import Path

from yuzzu.report import analyze_bond, plot_cash_flows


CURVE_PATH = Path("data/curve.csv")
MATURITY = 10
FACE_VALUE = 100.0
COUPON_RATE = 0.025
OUTPUT_CHART_PATH = Path("cash_flows.png")


def main():
    """Run a small end-to-end example using the Yuzzu package."""
    result = analyze_bond(
        maturity=MATURITY,
        face_value=FACE_VALUE,
        coupon_rate=COUPON_RATE,
        curve_path=CURVE_PATH,
    )

    print(f"Curve file: {CURVE_PATH}")
    print(f"Maturity: {MATURITY} years")
    print(f"Face value: {FACE_VALUE:.2f} EUR")
    print(f"Coupon rate: {COUPON_RATE * 100:.2f}%")
    print()
    print(f"Yield: {result['yield'] * 100:.2f}%")
    print(f"Price: {result['price']:.2f} EUR")
    print(f"Duration: {result['duration']:.2f} years")
    print()
    print("Cash flows:")
    for year, cash_flow in enumerate(result["cash_flows"], start=1):
        print(f"Year {year}: {cash_flow:.2f} EUR")

    chart_path = plot_cash_flows(result["cash_flows"], OUTPUT_CHART_PATH)
    print()
    print(f"Saved cash-flow chart to {chart_path}")


if __name__ == "__main__":
    main()
