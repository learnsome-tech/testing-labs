def test_review_questions_are_present():
    questions = {"timeout", "duplicate", "diagnose"}

    assert "timeout" in questions
    assert "duplicate" in questions
    assert "diagnose" in questions
