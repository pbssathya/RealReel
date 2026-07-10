from pathlib import Path

from realreel.models import Project

from realreel.models.production import Production


class ProjectParser:
    """
    Reads a RealReel project from disk.
    """

    def load(self, project_name: str) -> Project:

        project_root = Path("projects") / project_name

        if not project_root.exists():
            raise FileNotFoundError(
                f"Project '{project_name}' does not exist."
            )

        brief = project_root / "brief.md"

        if not brief.exists():
            raise FileNotFoundError(
                f"{brief} not found."
            )

        project = Project(
            name=project_name,
            root=project_root
        )

        project.description = brief.read_text(
            encoding="utf-8"
        )

        return project