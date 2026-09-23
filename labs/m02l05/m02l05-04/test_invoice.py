# Automated Testing, TDD & Quality Engineering — lesson m02l05 — Making Failures Explain Themselves
# https://learnsome.tech/courses/testing-course/watch?lesson=m02l05
# © LearnSome.tech
from invoice import line_names


def test_the_names_are_kept_in_order():
    lines = [("tea", 250), ("jam", 125)]

    assert line_names(lines) == ["tea", "jam", "cake"]
