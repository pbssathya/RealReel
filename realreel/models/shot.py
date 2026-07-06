from dataclasses import dataclass


@dataclass
class Shot:
    """Represents one shot in the timeline."""

    id: int

    narration: str = ""

    visual: str = ""

    animation: str = ""

    duration: float = 0.0

    avatar: bool = False

    music: str = ""