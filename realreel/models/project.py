from dataclasses import dataclass, field

from .production import Production


@dataclass
class Project:
    """
    Represents a long-lived creative project.

    A Project is a container that owns one or more
    Productions. It does not contain storytelling
    elements directly.
    """

    title: str = ""

    description: str = ""

    productions: list[Production] = field(default_factory=list)

    metadata: dict = field(default_factory=dict)

    def add_production(self, production: Production):
        """
        Adds a production to the project.
        """

        self.productions.append(production)
        