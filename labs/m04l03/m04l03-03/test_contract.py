# Automated Testing, TDD & Quality Engineering — lesson m04l03 — Contract Testing Between Services
# https://learnsome.tech/courses/testing-course/watch?lesson=m04l03
# © LearnSome.tech
def test_profile_contract():
    response = {"id": "u seven", "name": "Ada"}

    assert response["id"]
    assert response["name"] == "Ada"
