from invoice import line_names


def test_the_names_are_kept_in_order():
    lines = [("tea", 250), ("jam", 125)]

    assert line_names(lines) == ["tea", "jam", "cake"]
