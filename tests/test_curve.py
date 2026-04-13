import pytest
from pathlib import Path

from yuzzu.curve import YieldCurve


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


def test_curve_reads_csv_file(tmp_path: Path):
    curve_path = tmp_path / "curve.csv"
    write_curve_csv(curve_path)
    curve = YieldCurve(curve_path)

    assert curve.rate(1) == pytest.approx(0.01)
    assert curve.rate(10) == pytest.approx(0.055)


def test_curve_interpolates_between_known_points(tmp_path: Path):
    curve_path = tmp_path / "curve.csv"
    write_curve_csv(curve_path)
    curve = YieldCurve(curve_path)

    assert curve.rate(5.5) == pytest.approx(0.0325)
