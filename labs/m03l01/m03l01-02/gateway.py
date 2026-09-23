# Automated Testing, TDD & Quality Engineering — lesson m03l01 — What Test Doubles Are For
# https://learnsome.tech/courses/testing-course/watch?lesson=m03l01
# © LearnSome.tech
class GatewayTimeout(Exception):
    """The gateway did not answer in time."""


class Gateway:
    """The real client: one call, one card payment, real money."""

    def charge(self, pence, reference):
        raise RuntimeError("this would reach the network")
