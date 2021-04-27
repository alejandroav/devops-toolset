"""dotnet module literals"""

from core.app import App
from core.ValueDictsBase import ValueDictsBase

app: App = App()


class Literals(ValueDictsBase):
    """ValueDicts for the dotnet module."""

    _info = {
        "dotnet_restore_before": "Launching dotnet restore inside {path}. Please wait..",
        "dotnet_build_before": "Launching dotnet build inside {path}. Please wait..",
        "dotnet_publish_before": "Launching dotnet publish inside {path}. Please wait.."
    }
    _errors = {
        "dotnet_restore_err": "Something went wrong while restoring {path}. Please check the logs and try again.",
        "dotnet_build_err": "Something went wrong while building {path}. Please check the logs and try again.",
        "dotnet_publish_err": "Something went wrong while publishing in {path}. Please check the logs and try again."
    }

