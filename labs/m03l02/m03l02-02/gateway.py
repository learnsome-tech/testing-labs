# Automated Testing, TDD & Quality Engineering — lesson m03l02 — Fakes, Stubs, Mocks And Spies
# https://learnsome.tech/courses/testing-course/watch?lesson=m03l02
# © LearnSome.tech
class Gateway:
    """The real client: charge returns a receipt, or raises."""

    def charge(self, pence, reference):
        raise RuntimeError("this would reach the network")
