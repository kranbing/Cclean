from pathlib import Path


PROTECTED_PATHS = (
    Path("C:/Windows"),
    Path("C:/Program Files"),
    Path("C:/Program Files (x86)"),
)


def is_protected_path(path: Path) -> bool:
    resolved = path.resolve()
    return any(resolved == protected or protected in resolved.parents for protected in PROTECTED_PATHS)
