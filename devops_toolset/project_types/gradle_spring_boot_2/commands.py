"""spring boot 2 gradle module commands"""

from core.ValueDictsBase import ValueDictsBase
from core.app import App

app: App = App()


class Commands(ValueDictsBase):
    """ Commands for the  spring boot 2 gradle  module."""

    # Add your spring boot 2 gradle commands dictionaries here
    _commands = {
        "bootWar": "gradlew bootWar",
        "bootJar": "gradlew bootJar"
    }
