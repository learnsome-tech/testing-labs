import pytest

from discount import discounted


@pytest.mark.parametrize(
    "price, expected",
    [(1000, 900), (999, 899), (995, 896), (1, 1)],
)
def test_a_tenth_off(price, expected):
    assert discounted(price, 10) == expected
