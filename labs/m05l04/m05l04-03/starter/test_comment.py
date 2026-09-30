def test_comment_has_a_next_action():
    comment = "What happens after a timeout? Add a test for the retry limit."

    assert "timeout" in comment
    assert "Add a test" in comment
