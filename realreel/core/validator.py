from realreel.models.project import Project


class ProjectValidator:

    def validate(self, project: Project):

        errors = []

        if not project.title:
            errors.append("Missing project title.")

        if not project.platform:
            errors.append("Missing platform.")

        if project.duration <= 0:
            errors.append("Duration must be greater than zero.")

        if not project.language:
            errors.append("Missing language.")

        if errors:
            raise ValueError("\n".join(errors))

        return True
    