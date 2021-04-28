""" Init devops toolset

    Creates a global project variable which uses the Project class in order to accessç
    the different clis across project types.

    Project type will be determined in core/settings.json. Can be set also on configure.py
"""

import Project

global project

project = Project.Project()

import argparse
import json
import pkg_resources
import logging
from core.app import App
import Project
import devops_toolset

app = App()
logging.basicConfig(level=logging.INFO)
logging.Formatter("%(asctime)s %(levelname)-8s %(module)-15s %(message)s")
logger = logging.getLogger(__name__)


def configure(devops_platform: str, language: str, project_type: str, project_path: str):
    """ Sets the configuration inside settings.json and creates environment variables
    Arguments:
        devops_platform: Sets the target devops-platform to use.
        language: Sets the language
        project_type: Sets the project type to use
        project_path: Sets the project's path
    """
    settings_path = pkg_resources.resource_filename("core", "settings.json")

    with open(settings_path, 'r') as settings_file:
        settings = json.load(settings_file)
        logger.info(f"Retrieved settings.json from {settings_path}")

    settings['devops_platform'] = devops_platform
    settings['language'] = language
    settings['project_type'] = project_type
    settings['project_path'] = project_path

    with open(settings_path, 'w') as settings_file:
        logger.info(f"Setting 'devops_platform' -> {devops_platform}")
        logger.info(f"Setting 'language' -> {language}")
        logger.info(f"Setting 'project_type' -> {project_type}")
        logger.info(f"Setting 'project_path' -> {project_path}")
        json.dump(settings, settings_file)
        logger.info("Settings successfully saved")

    # Create environment variables using the platform-specific approach

    devops_platform = app.load_platform_specific("environment")
    devops_platform.create_environment_variables(settings)

    devops_toolset.project = Project.Project()
