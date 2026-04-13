from pathlib import Path

from yuzzu.report import analyze_bond, plot_cash_flows


def write_curve_csv(path: Path):
    path.write_text(
        "maturity,yield\n"
        "1,0.01\n"
        "2,0.015\n"
        "3,0.02\n"
        "4,0.025\n"
        "5,0.03\n"
        "6,0.035\n"
        "7,0.04\n"
        "8,0.045\n"
        "9,0.05\n"
        "10,0.055\n"
    )


def test_analyze_bond_returns_expected_keys(tmp_path: Path):
    curve_path = tmp_path / "curve.csv"
    write_curve_csv(curve_path)

    result = analyze_bond(
        maturity=4,
        face_value=100.0,
        coupon_rate=0.025,
        curve_path=curve_path,
    )

    assert set(result) == {"yield", "price", "duration", "cash_flows"}
    assert result["cash_flows"] == [2.5, 2.5, 2.5, 102.5]


def test_plot_cash_flows_writes_png(tmp_path: Path):
    curve_path = tmp_path / "curve.csv"
    write_curve_csv(curve_path)

    result = analyze_bond(
        maturity=3,
        face_value=100.0,
        coupon_rate=0.02,
        curve_path=curve_path,
    )

    output = plot_cash_flows(result["cash_flows"], tmp_path / "cash_flows.png")

    assert output.exists()
    assert output.suffix == ".png"
