# Automated Testing, TDD & Quality Engineering — lesson m03l02 — Fakes, Stubs, Mocks And Spies
# https://learnsome.tech/courses/testing-course/watch?lesson=m03l02
# © LearnSome.tech
from checkout import pay


class FakeGateway:
    """An in-memory gateway: real behaviour, no network, no money."""

    def __init__(self):
        self.ledger = {}

    def charge(self, pence, reference):
        if reference in self.ledger:
            raise RuntimeError("duplicate reference")
        self.ledger[reference] = pence
        return {"reference": reference}


def test_the_same_reference_cannot_be_charged_twice():
    fake = FakeGateway()

    pay(fake, 1000, "abc")

    assert fake.ledger == {"abc": 1000}
