# Automated Testing, TDD & Quality Engineering — lesson m03l05 — Testing The Filesystem
# https://learnsome.tech/courses/testing-course/watch?lesson=m03l05
# © LearnSome.tech
from pathlib import Path


def write_report(folder, name, text):
    path = Path(folder) / name
    path.write_text(text, encoding="utf-8")
    return path
