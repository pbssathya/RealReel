from realreel.models.project import Project


class ProjectValidator:
    """
    Validates a Project and its Productions.
    """

    def validate(self, project: Project):

        errors = []

        # ----------------------------------------------------------
        # Project Validation
        # ----------------------------------------------------------

        if not project.title:
            errors.append("Missing project title.")

        if not project.productions:
            errors.append("Project contains no productions.")

        # ----------------------------------------------------------
        # Production Validation
        # ----------------------------------------------------------

        for production in project.productions:

            if not production.title:
                errors.append("Missing production title.")

            if not production.platform:
                errors.append("Missing platform.")

            if production.duration <= 0:
                errors.append(
                    "Duration must be greater than zero."
                )

            if not production.language:
                errors.append("Missing language.")

        if errors:
            raise ValueError("\n".join(errors))

        return True
    