"""dotnet module commands"""

from core.ValueDictsBase import ValueDictsBase
from core.app import App

app: App = App()


class Commands(ValueDictsBase):
    """ Commands for the dotnet module."""

    # Add your dotnet commands dictionaries here
    _commands = {
        "dotnet_restore": "dotnet restore {args} {path}",
        "dotnet_build": "dotnet build {args} {path}",
        "dotnet_publish": "dotnet publish {args} {path}"
    }

