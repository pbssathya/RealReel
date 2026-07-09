from enum import Enum


class ProductionStatus(Enum):
    """
    Represents the lifecycle of a production.
    """

    DRAFT = "Draft"

    PLANNING = "Planning"

    STORY_READY = "Story Ready"

    VISUAL_READY = "Visual Ready"

    VOICE_READY = "Voice Ready"

    TIMELINE_READY = "Timeline Ready"

    RENDERING = "Rendering"

    RENDERED = "Rendered"

    REVIEW = "Review"

    PUBLISHED = "Published"

    ARCHIVED = "Archived"
    