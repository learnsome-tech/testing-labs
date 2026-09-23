# Automated Testing, TDD & Quality Engineering — lesson m03l03 — Why Over-Mocking Breeds False Positives
# https://learnsome.tech/courses/testing-course/watch?lesson=m03l03
# © LearnSome.tech
from checkout import pay


class ContractGateway:
    def charge(self, pence, reference):
        return {"reference": reference}


def test_pay_uses_the_gateway_contract():
    assert pay(ContractGateway(), 1000, "abc") == "abc"
