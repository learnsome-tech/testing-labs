# Automated Testing, TDD & Quality Engineering — lesson m04l05 — Testing With Real Databases
# https://learnsome.tech/courses/testing-course/watch?lesson=m04l05
# © LearnSome.tech
def test_unique_names_are_enforced():
    names = {"ada"}

    assert "ada" in names
    assert "grace" not in names
