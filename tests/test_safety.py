from pathlib import Path

from cclean.safety import is_protected_path


def test_windows_directory_is_protected() -> None:
    assert is_protected_path(Path("C:/Windows/Temp"))


def test_user_temp_directory_is_not_protected() -> None:
    assert not is_protected_path(Path("C:/Users/example/AppData/Local/Temp"))
