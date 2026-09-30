from report import read_report, write_report


def test_missing_report_is_empty(tmp_path):
    assert read_report(tmp_path, "daily.txt") is None


def test_existing_report_can_be_read(tmp_path):
    write_report(tmp_path, "daily.txt", "ready")

    assert read_report(tmp_path, "daily.txt") == "ready"
