# Automated Testing, TDD & Quality Engineering — lesson m01l05 — Coverage: Diagnostic, Not Target
# https://learnsome.tech/courses/testing-course/watch?lesson=m01l05
# © LearnSome.tech
from refund import refund


def test_a_full_return_gives_everything_back():
    assert refund(1000, 1000) == 0


def test_a_part_return_keeps_the_difference():
    assert refund(1000, 250) == 750
