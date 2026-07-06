from dataclasses import dataclass
from pathlib import Path


@dataclass
class Asset:
    """Represents any project asset."""

    name: str
    type: str
    path: Path