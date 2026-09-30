def test_an_entry_can_be_added(ledger):
    ledger.append(("tea", 250))
    assert len(ledger) == 1


def test_each_test_gets_a_fresh_ledger(ledger):
    assert ledger == []
