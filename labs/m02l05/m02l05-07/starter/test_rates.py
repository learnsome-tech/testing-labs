import pytest

from rates import convert, rate_for


def test_a_conversion_is_right_to_the_penny():
    assert convert(7, "EUR") == pytest.approx(8.246)


def test_an_unknown_currency_is_refused():
    with pytest.raises(KeyError, match="MOON"):
        rate_for("MOON")
