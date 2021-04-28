""" Init devops toolset

    Creates a global project variable which uses the Project class in order to accessç
    the different clis across project types.

    Project type will be determined in core/settings.json. Can be set also on configure.py
"""

import Project

global project

project = Project.Project()
