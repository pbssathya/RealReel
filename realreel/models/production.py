from dataclasses import dataclass, field

from .production_status import ProductionStatus


@dataclass
class Production:
    """
    Represents the complete state of a production
    as it evolves from an idea into publish-ready content.
    """

    # ------------------------------------------------------------------
    # Core Attributes
    # ------------------------------------------------------------------

    status: ProductionStatus = ProductionStatus.DRAFT

    scenes: list = field(default_factory=list)

    assets: list = field(default_factory=list)

    timeline = None

    deliverables: list = field(default_factory=list)

    metadata: dict = field(default_factory=dict)

    history: list = field(default_factory=list)

    # ------------------------------------------------------------------
    # Business Methods
    # ------------------------------------------------------------------

    def add_scene(self, scene):
        """
        Adds a scene to the production.
        """

        self.scenes.append(scene)

        self.history.append(
            f"Scene added ({len(self.scenes)} total)"
        )
        