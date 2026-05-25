from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class CleanupCategory:
    key: str
    name: str
    description: str
    requires_admin: bool = False


@dataclass(frozen=True)
class ScanResult:
    category: CleanupCategory
    total_bytes: int
    file_count: int
    paths: tuple[Path, ...] = ()
