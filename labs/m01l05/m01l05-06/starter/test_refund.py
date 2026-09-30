from refund import refund


def test_a_restocking_fee_comes_off_the_refund():
    assert refund(1000, 1000, restocking_fee=50) == 950
