# Automated Testing, TDD & Quality Engineering — lesson m03l04 — Testing Time And Randomness
# https://learnsome.tech/courses/testing-course/watch?lesson=m03l04
# © LearnSome.tech
from datetime import datetime, timezone


def active(expires_at, now=None):
    now = now or datetime.now(timezone.utc)
    return now < expires_at
