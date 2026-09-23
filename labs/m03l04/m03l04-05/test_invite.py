# Automated Testing, TDD & Quality Engineering — lesson m03l04 — Testing Time And Randomness
# https://learnsome.tech/courses/testing-course/watch?lesson=m03l04
# © LearnSome.tech
from invite import code


class RedChoice:
    def choice(self, options):
        return "red"


def test_code_uses_the_generator_result():
    assert code(RedChoice()) == "red"
