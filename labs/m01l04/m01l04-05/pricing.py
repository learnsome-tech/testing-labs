# Automated Testing, TDD & Quality Engineering — lesson m01l04 — The Test Pyramid And Where It Is Wrong
# https://learnsome.tech/courses/testing-course/watch?lesson=m01l04
# © LearnSome.tech
def subtotal(lines):
    """Total of (price in pence, count) lines."""
    return sum(price * count for price, count in lines)


def with_vat(amount, rate=20):
    """Amount plus value added tax, to the nearest penny."""
    return round(amount * (100 + rate) / 100)
