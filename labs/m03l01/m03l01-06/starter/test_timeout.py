from checkout import pay
from gateway import GatewayTimeout


class TimingOutGateway:
    """Never answers, the way the real one does under load."""

    def charge(self, pence, reference):
        raise GatewayTimeout("no answer in three seconds")


def test_a_timeout_leaves_the_customer_with_nothing():
    assert pay(TimingOutGateway(), 1000, "abc") is None
