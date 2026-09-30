from unittest.mock import create_autospec

from checkout import pay


class Gateway:
    def charge(self, pence, reference):
        return {"reference": reference}


def test_pay_returns_the_gateway_id():
    gateway = create_autospec(Gateway, instance=True)
    gateway.charge.return_value = {"id": "abc"}

    assert pay(gateway, 1000, "abc") == "abc"
