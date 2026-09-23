# Automated Testing, TDD & Quality Engineering — lesson m02l02 — Parametrised Tests
# https://learnsome.tech/courses/testing-course/watch?lesson=m02l02
# © LearnSome.tech
def discounted(price, percent):
    """Price in pence after a whole number percentage discount."""
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between zero and a hundred")
    return int(price * (100 - percent) / 100)
