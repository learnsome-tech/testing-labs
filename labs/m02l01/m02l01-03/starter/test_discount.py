import pytest

from discount import discounted


def test_ten_per_cent_off_a_round_price():
    assert discounted(1000, 10) == 900


def test_nothing_off_leaves_the_price_alone():
    assert discounted(1000, 0) == 1000


def test_a_silly_percentage_is_refused():
    with pytest.raises(ValueError):
        discounted(1000, 120)
