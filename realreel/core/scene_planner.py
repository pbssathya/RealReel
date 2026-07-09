from realreel.models.shot import Shot


class ScenePlanner:

    def plan(self, project):

        total = project.duration

        shot_length = 5

        count = max(1, total // shot_length)

        project.shots = []

        for i in range(count):

            project.shots.append(
                Shot(
                    number=i + 1,
                    duration=shot_length
                )
            )

        return project
    