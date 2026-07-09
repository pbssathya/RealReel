from dataclasses import dataclass


@dataclass
class Shot:

    number: int

    duration: int

    purpose: str = ""

    narration: str = ""

    visual: str = ""

    image_prompt: str = ""

    camera: str = ""

    transition: str = ""

    emotion: str = ""
    