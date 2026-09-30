import random


def code(generator=None):
    generator = generator or random
    return generator.choice(["red", "blue", "green"])
