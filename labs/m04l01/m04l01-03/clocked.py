# Automated Testing, TDD & Quality Engineering — lesson m04l01 — Flaky Tests And How To Kill Them
# https://learnsome.tech/courses/testing-course/watch?lesson=m04l01
# © LearnSome.tech
from datetime import datetime, timezone


def second(now=None):
    now = now or datetime.now(timezone.utc)
    return now.second
