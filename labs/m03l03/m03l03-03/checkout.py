# Automated Testing, TDD & Quality Engineering — lesson m03l03 — Why Over-Mocking Breeds False Positives
# https://learnsome.tech/courses/testing-course/watch?lesson=m03l03
# © LearnSome.tech
def pay(gateway, pence, reference):
    receipt = gateway.charge(pence, reference)
    return receipt["id"]
