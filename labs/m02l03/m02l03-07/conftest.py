# Automated Testing, TDD & Quality Engineering — lesson m02l03 — Fixtures And Their Scope
# https://learnsome.tech/courses/testing-course/watch?lesson=m02l03
# © LearnSome.tech
import pytest


@pytest.fixture
def ledger():
    print("open the ledger")
    entries = []
    yield entries
    print("close the ledger, entries:", len(entries))
