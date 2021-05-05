"""spring boot 2 gradle module literals"""

from core.app import App
from core.ValueDictsBase import ValueDictsBase

app: App = App()


class Literals(ValueDictsBase):
    """ValueDicts for the spring boot 2 gradle module."""

    _info = {
        "gradle_spring_boot_build_before": "Running {task} task. Please wait...",
        "gradle_spring_boot_build_after": "Task {task} completed."
    }
    _errors = {
        "gradle_spring_boot_build_err": "Something went wrong during the {task} task. Please check the logs and try "
                                        "again. "
    }
