# Automated Testing, TDD & Quality Engineering — lesson m03l05 — Testing The Filesystem
# https://learnsome.tech/courses/testing-course/watch?lesson=m03l05
# © LearnSome.tech
from report import write_report


def test_report_is_written_with_utf_eight(tmp_path):
    path = write_report(tmp_path, "daily.txt", "ready")

    assert path.name == "daily.txt"
    assert path.read_text(encoding="utf-8") == "ready"
    assert path.parent == tmp_path
