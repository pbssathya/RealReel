from realreel.providers.base import StoryProvider


class OpenAIStoryProvider(StoryProvider):
    """
    OpenAI implementation of the StoryProvider interface.
    """

    def generate_story(self, project):
        """
        Temporary stub.

        A future implementation will generate
        story content using the configured OpenAI model.
        """

        return project
    