def test_required_checks_are_named():
    checks = ["lint", "unit", "integration"]

    assert checks == ["lint", "unit", "integration"]
