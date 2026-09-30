import pytest


@pytest.fixture
def basket():
    print("building a basket")
    return [(250, 2), (125, 4)]


@pytest.fixture(scope="module")
def price_list():
    print("loading the price list")
    return {"tea": 250, "jam": 125}
