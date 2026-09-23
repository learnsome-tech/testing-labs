# Automated Testing, TDD & Quality Engineering — lesson m01l01 — The Cost And Value Of A Test
# https://learnsome.tech/courses/testing-course/watch?lesson=m01l01
# © LearnSome.tech
from cart import total


def test_two_lines_add_up():
    assert total([(250, 2), (125, 4)]) == 1000
