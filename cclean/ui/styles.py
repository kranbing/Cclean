from pathlib import Path


def load_stylesheet() -> str:
    stylesheet_path = Path(__file__).with_name("styles.qss")
    if not stylesheet_path.exists():
        return ""
    return stylesheet_path.read_text(encoding="utf-8")
