import json
from pathlib import Path


class ProductionPlanner:
    """
    Builds the Production Specification for a project.
    """

    def build(self, project, output_file):

        if not project.productions:
            raise ValueError(
                "Project contains no productions."
            )

        production = project.productions[0]

        specification = {

            "schema_version": "0.2",

            "project": {

                "title": project.title,
                "description": project.description,

            },

            "production": {

                "title": production.title,
                "platform": production.platform,
                "duration": production.duration,
                "language": production.language,
                "audience": production.audience,
                "tone": production.tone,
                "status": production.status.name,

            },

            "scenes": []

        }

        output = Path(output_file)

        output.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        output.write_text(
            json.dumps(
                specification,
                indent=4
            ),
            encoding="utf-8"
        )

        return output
    