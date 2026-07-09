from pathlib import Path

from realreel.models.project import Project


class BriefParser:

    def parse(self, filepath):

        path = Path(filepath)

        if not path.exists():
            raise FileNotFoundError(filepath)

        lines = path.read_text(
            encoding="utf-8"
        ).splitlines()

        project = Project()

        description = []

        for line in lines:

            line = line.strip()

            if not line:
                continue

            if line.startswith("# "):
                project.title = line[2:].strip()

            elif ":" in line:

                key, value = line.split(":", 1)

                key = key.strip().lower()
                value = value.strip()

                if key == "platform":
                    project.platform = value

                elif key == "duration":
                    project.duration = int(value)

                elif key == "language":
                    project.language = value

                elif key == "target audience":
                    project.audience = value

                elif key == "tone":
                    project.tone = value

                else:
                    description.append(line)

            else:
                description.append(line)

        project.description = "\n".join(description)

        return project
    