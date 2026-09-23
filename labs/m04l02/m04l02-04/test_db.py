# Automated Testing, TDD & Quality Engineering — lesson m04l02 — Integration Testing With Containers
# https://learnsome.tech/courses/testing-course/watch?lesson=m04l02
# © LearnSome.tech
import pytest


@pytest.fixture
def database():
    container = start_postgres_image()
    yield container.connection
    container.stop()


def test_health_check(database):
    assert database.execute("select 1") == 1
