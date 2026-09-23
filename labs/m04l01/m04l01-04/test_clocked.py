# Automated Testing, TDD & Quality Engineering — lesson m04l01 — Flaky Tests And How To Kill Them
# https://learnsome.tech/courses/testing-course/watch?lesson=m04l01
# © LearnSome.tech
from datetime import datetime, timezone

from clocked import second


def test_second_reads_the_supplied_instant():
    now = datetime(2030, 1, 1, 12, 34, 56, tzinfo=timezone.utc)
    assert second(now) == 56
