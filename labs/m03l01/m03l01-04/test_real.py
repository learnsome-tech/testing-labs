# Automated Testing, TDD & Quality Engineering — lesson m03l01 — What Test Doubles Are For
# https://learnsome.tech/courses/testing-course/watch?lesson=m03l01
# © LearnSome.tech
from checkout import pay
from gateway import Gateway


def test_paying_with_the_real_gateway():
    assert pay(Gateway(), 1000, "abc") == "abc"
