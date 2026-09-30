from pathlib import Path


def write_report(folder, name, text):
    path = Path(folder) / name
    path.write_text(text, encoding="utf-8")
    return path
