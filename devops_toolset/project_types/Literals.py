"""project_types common module

   Place here all project common related literals

"""

from core.app import App
from core.ValueDictsBase import ValueDictsBase

app: App = App()


class Literals(ValueDictsBase):
    """ValueDicts for the project_types module."""

    _info = {
        "phase_start": "Starting [{phase_name}] phase.",
        "phase_end": "Finished [{phase_name}] phase.",
    }
    _errors = {
    }

