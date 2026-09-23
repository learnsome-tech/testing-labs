# Automated Testing, TDD & Quality Engineering — lesson m02l02 — Parametrised Tests
# https://learnsome.tech/courses/testing-course/watch?lesson=m02l02
# © LearnSome.tech
import pytest

from discount import discounted


@pytest.mark.parametrize(
    "price, expected",
    [(1000, 900), (999, 899), (995, 896), (1, 1)],
    ids=["round", "off-by-a-penny", "half-penny", "single-penny"],
)
def test_a_tenth_off(price, expected):
    assert discounted(price, 10) == expected
