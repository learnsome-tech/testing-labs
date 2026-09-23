# Automated Testing, TDD & Quality Engineering — lesson m02l03 — Fixtures And Their Scope
# https://learnsome.tech/courses/testing-course/watch?lesson=m02l03
# © LearnSome.tech
def test_an_entry_can_be_added(ledger):
    ledger.append(("tea", 250))
    assert len(ledger) == 1


def test_each_test_gets_a_fresh_ledger(ledger):
    assert ledger == []
