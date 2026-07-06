from dataclasses import dataclass, field
from pathlib import Path

from .shot import Shot
from .asset import Asset


@dataclass
class Project:
    """Represents a complete RealReel project."""

    name: str
    root: Path

    title: str = ""
    description: str = ""
    language: str = "en"

    shots: list[Shot] = field(default_factory=list)
    assets: list[Asset] = field(default_factory=list)

    status: str = "created"

    def add_shot(self, shot: Shot):
        self.shots.append(shot)

    def add_asset(self, asset: Asset):
        self.assets.append(asset)

    @property
    def shot_count(self):
        return len(self.shots)