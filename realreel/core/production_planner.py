import json
from pathlib import Path


class ProductionPlanner:

    def build(self, project, output_file):

        production = {

            "project": {
                "title": project.title,
                "platform": project.platform,
                "duration": project.duration,
                "language": project.language,
                "audience": project.audience,
                "tone": project.tone,
                "description": project.description,
            },

            "shots": [

                {
                    "number": shot.number,
                    "purpose": shot.purpose,
                    "duration": shot.duration,
                    "narration": shot.narration,
                    "visual": shot.visual,
                    "camera": shot.camera,
                    "emotion": shot.emotion,
                    "transition": shot.transition,
                    "image_prompt": shot.image_prompt,
                }

                for shot in project.shots

            ]
        }

        output = Path(output_file)

        output.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        output.write_text(
            json.dumps(
                production,
                indent=4
            ),
            encoding="utf-8"
        )

        return output
    