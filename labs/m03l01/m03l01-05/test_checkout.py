# Automated Testing, TDD & Quality Engineering — lesson m03l01 — What Test Doubles Are For
# https://learnsome.tech/courses/testing-course/watch?lesson=m03l01
# © LearnSome.tech
from checkout import pay


class StubGateway:
    """Answers one way, always, and records nothing."""

    def charge(self, pence, reference):
        return {"reference": reference}


def test_a_successful_charge_returns_the_reference():
    assert pay(StubGateway(), 1000, "abc") == "abc"
