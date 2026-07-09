class ProviderManager:
    """
    Responsible for returning the configured provider
    for each AI capability.
    """

    def get_story_provider(self):
        raise NotImplementedError("No Story Provider configured.")

    def get_image_provider(self):
        raise NotImplementedError("No Image Provider configured.")

    def get_voice_provider(self):
        raise NotImplementedError("No Voice Provider configured.")
    