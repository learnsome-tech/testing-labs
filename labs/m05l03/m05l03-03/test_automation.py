# Automated Testing, TDD & Quality Engineering — lesson m05l03 — What To Automate Away
# https://learnsome.tech/courses/testing-course/watch?lesson=m05l03
# © LearnSome.tech
def test_required_checks_are_named():
    checks = ["lint", "unit", "integration"]

    assert checks == ["lint", "unit", "integration"]
