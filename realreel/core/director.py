from realreel.models.shot import Shot


class CreativeDirector:

    def create_story(self, project):

        project.shots = [

            Shot(
                number=1,
                duration=5,
                purpose="Hook"
            ),

            Shot(
                number=2,
                duration=10,
                purpose="Introduction"
            ),

            Shot(
                number=3,
                duration=20,
                purpose="Main Content"
            ),

            Shot(
                number=4,
                duration=15,
                purpose="Climax"
            ),

            Shot(
                number=5,
                duration=10,
                purpose="Call To Action"
            )

        ]

        return project
    