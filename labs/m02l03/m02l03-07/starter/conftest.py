import pytest


@pytest.fixture
def ledger():
    print("open the ledger")
    entries = []
    yield entries
    print("close the ledger, entries:", len(entries))
