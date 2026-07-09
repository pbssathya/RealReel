class StoryAgent:
    """
    Responsible for generating the complete story
    for a production.

    The StoryAgent does not know which AI provider
    is being used. It delegates that responsibility
    to the ProviderManager.
    """

    def __init__(self, provider_manager):
        self.provider_manager = provider_manager

    def generate(self, project):
        provider = self.provider_manager.get_story_provider()
        return provider.generate_story(project)
    