from pathlib import Path

from realreel.models import Project
from realreel.models.production import Production


class BriefParser:
    """
    Parses a project brief and constructs the initial
    Project and Production domain objects.
    """

    def parse(self, brief_file: Path) -> Project:

        if not brief_file.exists():
            raise FileNotFoundError(
                f"{brief_file} not found."
            )

        project = Project()
        production = Production()

        description = []

        for line in brief_file.read_text(
            encoding="utf-8"
        ).splitlines():

            line = line.strip()

            if not line:
                continue

            if line.startswith("# "):
                title = line[2:].strip()

                project.title = title
                production.title = title

                continue

            if ":" in line:

                key, value = line.split(":", 1)

                key = key.strip().lower()
                value = value.strip()

                if key == "platform":
                    production.platform = value

                elif key == "duration":
                    production.duration = int(value)

                elif key == "language":
                    production.language = value

                elif key == "audience":
                    production.audience = value

                elif key == "tone":
                    production.tone = value

                continue

            description.append(line)

        project.description = "\n".join(description)

        project.add_production(production)

        return project
    