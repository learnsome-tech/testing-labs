# Automated Testing, TDD & Quality Engineering — lesson m01l01 — The Cost And Value Of A Test
# https://learnsome.tech/courses/testing-course/watch?lesson=m01l01
# © LearnSome.tech
def total(lines):
    """Total of (price in pence, count) lines, less a launch discount."""
    subtotal = sum(price * count for price, count in lines)
    return subtotal - 100
