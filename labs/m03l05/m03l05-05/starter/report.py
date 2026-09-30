from pathlib import Path

def write_report(folder, name, text):
    path = Path(folder) / name
    path.write_text(text, encoding="utf-8")
    return path

def read_report(folder, name):
    path = Path(folder) / name
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")
