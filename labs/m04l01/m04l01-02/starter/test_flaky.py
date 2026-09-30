from datetime import datetime, timezone


def test_second_is_zero():
    now = datetime.now(timezone.utc)
    assert now.second == 0
