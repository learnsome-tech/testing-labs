def test_the_basket_has_two_lines(basket, price_list):
    assert len(basket) == 2


def test_the_price_list_knows_tea(basket, price_list):
    assert price_list["tea"] == 250
