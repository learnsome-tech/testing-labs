# Automated Testing, TDD & Quality Engineering — lesson m01l03 — One Assertion Per Reason
# https://learnsome.tech/courses/testing-course/watch?lesson=m01l03
# © LearnSome.tech
from pricing import subtotal, with_vat


def test_subtotal_adds_the_lines():
    assert subtotal([(250, 2)]) == 500


def test_the_default_rate_is_twenty():
    assert with_vat(1000) == 1200


def test_vat_rounds_to_the_penny():
    assert with_vat(999) == 1199
