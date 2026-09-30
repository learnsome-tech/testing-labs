from unittest.mock import create_autospec

from checkout import pay
from gateway import Gateway


def test_the_gateway_is_charged_once_with_the_basket_total():
    gateway = create_autospec(Gateway, instance=True)
    gateway.charge.return_value = {"reference": "abc"}

    pay(gateway, 1000, "abc")

    gateway.charge.assert_called_once_with(1000, "abc")
