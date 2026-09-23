# Automated Testing, TDD & Quality Engineering — lesson m03l01 — What Test Doubles Are For
# https://learnsome.tech/courses/testing-course/watch?lesson=m03l01
# © LearnSome.tech
from gateway import GatewayTimeout


def pay(gateway, pence, reference):
    """Charge a basket, or report that the gateway did not answer."""
    try:
        receipt = gateway.charge(pence, reference)
    except GatewayTimeout:
        return None
    return receipt["reference"]
