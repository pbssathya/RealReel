from abc import ABC, abstractmethod


class StoryProvider(ABC):
    """
    Base class for all story generation providers.
    """

    @abstractmethod
    def generate_story(self, project):
        pass


class ImageProvider(ABC):
    """
    Base class for all image generation providers.
    """

    @abstractmethod
    def generate_images(self, project):
        pass


class VoiceProvider(ABC):
    """
    Base class for all voice generation providers.
    """

    @abstractmethod
    def generate_voice(self, project):
        pass
    