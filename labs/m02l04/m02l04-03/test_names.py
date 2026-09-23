# Automated Testing, TDD & Quality Engineering — lesson m02l04 — Naming Tests For Readability
# https://learnsome.tech/courses/testing-course/watch?lesson=m02l04
# © LearnSome.tech
from discount import discounted


def test_discount1():
    assert discounted(1000, 10) == 900


def test_discount2():
    assert discounted(1000, 0) == 1000


def test_discount_edge():
    assert discounted(1000, 100) == 0
