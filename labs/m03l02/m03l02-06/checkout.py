# Automated Testing, TDD & Quality Engineering — lesson m03l02 — Fakes, Stubs, Mocks And Spies
# https://learnsome.tech/courses/testing-course/watch?lesson=m03l02
# © LearnSome.tech
def pay(gateway, pence, reference):
    return gateway.charge(pence, reference)["reference"]
