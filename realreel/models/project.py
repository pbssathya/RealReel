from dataclasses import dataclass, field

from realreel.models.shot import Shot


@dataclass
class Project:

    title: str = ""

    platform: str = ""

    duration: int = 60

    language: str = "English"

    audience: str = ""

    tone: str = ""

    description: str = ""

    shots: list[Shot] = field(default_factory=list)

    metadata: dict = field(default_factory=dict)
    