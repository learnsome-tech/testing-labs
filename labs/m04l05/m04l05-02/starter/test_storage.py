def test_unique_names_are_enforced():
    names = {"ada"}

    assert "ada" in names
    assert "grace" not in names
