# Automated Testing, TDD & Quality Engineering — lesson m01l05 — Coverage: Diagnostic, Not Target
# https://learnsome.tech/courses/testing-course/watch?lesson=m01l05
# © LearnSome.tech
from refund import refund


def test_every_line_runs():
    refund(1000, 1000)
    refund(1000, 250, restocking_fee=50)
    try:
        refund(100, 500)
    except ValueError:
        pass
