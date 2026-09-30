import pytest


@pytest.fixture
def database():
    container = start_postgres_image()
    yield container.connection
    container.stop()


def test_health_check(database):
    assert database.execute("select 1") == 1
