# Automated Testing, TDD & Quality Engineering — lesson m03l04 — Testing Time And Randomness
# https://learnsome.tech/courses/testing-course/watch?lesson=m03l04
# © LearnSome.tech
from datetime import datetime, timezone

from session import active


NOW = datetime(2030, 1, 1, tzinfo=timezone.utc)


def test_session_is_active_before_expiry():
    assert active(NOW.replace(second=1), NOW) is True


def test_session_is_inactive_at_expiry():
    assert active(NOW, NOW) is False
