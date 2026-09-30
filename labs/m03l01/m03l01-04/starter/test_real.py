from checkout import pay
from gateway import Gateway


def test_paying_with_the_real_gateway():
    assert pay(Gateway(), 1000, "abc") == "abc"
