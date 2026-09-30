from datetime import datetime, timezone


def active(expires_at, now=None):
    now = now or datetime.now(timezone.utc)
    return now < expires_at
