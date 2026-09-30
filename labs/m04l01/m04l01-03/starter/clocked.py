from datetime import datetime, timezone


def second(now=None):
    now = now or datetime.now(timezone.utc)
    return now.second
