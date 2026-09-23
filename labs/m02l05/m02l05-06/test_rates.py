# Automated Testing, TDD & Quality Engineering — lesson m02l05 — Making Failures Explain Themselves
# https://learnsome.tech/courses/testing-course/watch?lesson=m02l05
# © LearnSome.tech
from rates import convert


def test_a_conversion_is_exact():
    assert convert(7, "EUR") == 8.246
