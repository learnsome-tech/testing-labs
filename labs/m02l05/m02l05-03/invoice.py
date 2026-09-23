# Automated Testing, TDD & Quality Engineering — lesson m02l05 — Making Failures Explain Themselves
# https://learnsome.tech/courses/testing-course/watch?lesson=m02l05
# © LearnSome.tech
def invoice_total(lines):
    """Total pence on an invoice, before tax."""
    return sum(price * count for price, count in lines)


def line_names(lines):
    """The names on the invoice, in the order they were added."""
    return [name for name, _price in lines]
