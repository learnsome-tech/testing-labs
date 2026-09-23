# Automated Testing, TDD & Quality Engineering — lesson m02l05 — Making Failures Explain Themselves
# https://learnsome.tech/courses/testing-course/watch?lesson=m02l05
# © LearnSome.tech
from invoice import invoice_total


def test_the_invoice_adds_up_every_line():
    lines = [(250, 2), (125, 4)]

    total = invoice_total(lines)

    assert total == 1100
