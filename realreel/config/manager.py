from pathlib import Path

import yaml


class ConfigManager:
    """
    Loads and provides access to RealReel configuration.
    """

    def __init__(self):
        self._config = {}

    def load(self):

        config_file = Path("config") / "engine.yaml"

        if not config_file.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {config_file}"
            )

        with open(config_file, "r", encoding="utf-8") as file:
            self._config = yaml.safe_load(file)

        return self

    @property
    def data(self):
        return self._config

    @property
    def paths(self):
        return self._config.get("paths", {})

    @property
    def defaults(self):
        return self._config.get("defaults", {})

    @property
    def creator(self):
        return self._config.get("creator", {})

    @property
    def logging(self):
        return self._config.get("logging", {})
    