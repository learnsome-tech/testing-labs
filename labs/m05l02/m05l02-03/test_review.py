# Automated Testing, TDD & Quality Engineering — lesson m05l02 — What To Look For In A Review
# https://learnsome.tech/courses/testing-course/watch?lesson=m05l02
# © LearnSome.tech
def test_review_questions_are_present():
    questions = {"timeout", "duplicate", "diagnose"}

    assert "timeout" in questions
    assert "duplicate" in questions
    assert "diagnose" in questions
