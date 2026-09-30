from invoice import invoice_total


def test_the_invoice_adds_up_every_line():
    lines = [(250, 2), (125, 4)]

    total = invoice_total(lines)

    assert total == 1100
