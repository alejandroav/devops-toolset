"""Loads settings from the settings.json file"""

import pathlib
import os
import json


class Settings(object):
    """Application settings"""

    _DEVOPS: str = "devops"
    _LOCALES: str = "locales"
    _CORE: str = "core"
    _CONFIG_SETTINGS_FILE_NAME: str = "logging-config.json"
    _CURRENT_PATH: str = os.path.dirname(os.path.realpath(__file__))

    # defaults
    root_path: pathlib.Path = pathlib.Path(_CURRENT_PATH).parent.absolute()
    devops_path: pathlib.Path = pathlib.Path.joinpath(root_path, _DEVOPS).absolute()
    locales_path: pathlib.Path = pathlib.Path.joinpath(root_path, _LOCALES).absolute()
    log_config_file_path: pathlib.Path = pathlib.Path.joinpath(root_path, _CORE, _CONFIG_SETTINGS_FILE_NAME).absolute()
    language: str = "en"
    platform: str = "azuredevops"
    platform_specific_path: pathlib.Path = pathlib.Path.joinpath(devops_path, platform).absolute()

    def __init__(self):
        """Loads settings"""

        self.load(self._CURRENT_PATH)
        self.platform_specific_path = pathlib.Path.joinpath(self.devops_path, self.platform).absolute()

    @staticmethod
    def read_settings_from_file(path: str):
        """Loads settings from settings.json

        Args:
            path: Path to read settings.json from
        """

        with open(os.path.join(path, "settings.json"), "r") as settings_file:
            settings = json.load(settings_file)

        return settings

    def load(self, path: str):
        """Assigns settings"""

        settings = self.read_settings_from_file(path)

        # Add your setting mappings here
        self.language = settings["language"]
        self.platform = settings["platform"]
