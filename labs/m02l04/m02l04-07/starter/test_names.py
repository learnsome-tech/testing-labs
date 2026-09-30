from discount import discounted


def test_a_tenth_off_a_thousand_pence_leaves_nine_hundred():
    assert discounted(1000, 10) == 900


def test_no_discount_leaves_the_price_untouched():
    assert discounted(1000, 0) == 1000


def test_a_full_discount_makes_the_price_zero():
    assert discounted(1000, 100) == 0
