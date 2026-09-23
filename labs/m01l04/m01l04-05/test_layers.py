# Automated Testing, TDD & Quality Engineering — lesson m01l04 — The Test Pyramid And Where It Is Wrong
# https://learnsome.tech/courses/testing-course/watch?lesson=m01l04
# © LearnSome.tech
import time

import pytest

from pricing import subtotal, with_vat


def test_vat_rounds_to_the_penny():
    assert with_vat(999) == 1199


@pytest.mark.slow
def test_the_price_service_answers():
    time.sleep(0.35)
    assert with_vat(subtotal([(100, 1)])) == 120
