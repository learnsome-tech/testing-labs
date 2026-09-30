from report import write_report


def test_report_is_written_with_utf_eight(tmp_path):
    path = write_report(tmp_path, "daily.txt", "ready")

    assert path.name == "daily.txt"
    assert path.read_text(encoding="utf-8") == "ready"
    assert path.parent == tmp_path
