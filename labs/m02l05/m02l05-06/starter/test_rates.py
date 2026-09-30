from rates import convert


def test_a_conversion_is_exact():
    assert convert(7, "EUR") == 8.246
