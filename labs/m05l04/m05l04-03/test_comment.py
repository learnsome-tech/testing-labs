# Automated Testing, TDD & Quality Engineering — lesson m05l04 — Writing Actionable Review Comments
# https://learnsome.tech/courses/testing-course/watch?lesson=m05l04
# © LearnSome.tech
def test_comment_has_a_next_action():
    comment = "What happens after a timeout? Add a test for the retry limit."

    assert "timeout" in comment
    assert "Add a test" in comment
