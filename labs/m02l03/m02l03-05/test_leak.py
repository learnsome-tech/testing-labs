# Automated Testing, TDD & Quality Engineering — lesson m02l03 — Fixtures And Their Scope
# https://learnsome.tech/courses/testing-course/watch?lesson=m02l03
# © LearnSome.tech
def test_adding_a_line(price_list):
    price_list["cake"] = 400
    assert len(price_list) == 3


def test_the_price_list_is_untouched(price_list):
    assert len(price_list) == 2
