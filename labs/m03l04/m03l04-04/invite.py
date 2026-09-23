# Automated Testing, TDD & Quality Engineering — lesson m03l04 — Testing Time And Randomness
# https://learnsome.tech/courses/testing-course/watch?lesson=m03l04
# © LearnSome.tech
import random


def code(generator=None):
    generator = generator or random
    return generator.choice(["red", "blue", "green"])
