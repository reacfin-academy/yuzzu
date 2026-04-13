import pytest

from yuzzu.bond import Bond


def test_cash_flows_include_principal_at_maturity():
    bond = Bond(maturity=3, face_value=100.0, coupon_rate=0.05)

    assert bond.cash_flows == [5.0, 5.0, 105.0]


def test_price_is_par_when_coupon_matches_yield():
    bond = Bond(maturity=10, face_value=100.0, coupon_rate=0.05)

    assert bond.price(0.05) == pytest.approx(100.0)


def test_duration_is_between_zero_and_maturity():
    bond = Bond(maturity=5, face_value=100.0, coupon_rate=0.03)

    duration = bond.duration(0.04)

    assert 0 < duration < bond.maturity
