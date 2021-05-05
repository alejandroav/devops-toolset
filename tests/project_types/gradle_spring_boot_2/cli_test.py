""" Unit-core for the dotnet/cli.py module"""

from unittest.mock import patch, call
import pytest

import project_types.gradle_spring_boot_2.cli as sut
from core.CommandsCore import CommandsCore
from core.LiteralsCore import LiteralsCore
from project_types.gradle_spring_boot_2.commands import Commands
from project_types.gradle_spring_boot_2.Literals import Literals
from core.app import App

app: App = App()
literals = LiteralsCore([Literals])
commands = CommandsCore([Commands])


@patch("tools.cli.call_subprocess")
def test_build_calls_bootjar_by_default(subprocess_mock):
    task = "bootJar"
    command = commands.get(task)
    literal_before = literals.get("gradle_spring_boot_build_before").format(task=task)
    literal_after = literals.get("gradle_spring_boot_build_after").format(task=task)
    literal_error = literals.get("gradle_spring_boot_build_err").format(task=task)

    sut.build()

    subprocess_mock.assert_called_once_with(
        command,
        log_before_out=[literal_before],
        log_after_out=[literal_after],
        log_after_err=[literal_error]
    )


@patch("tools.cli.call_subprocess")
def test_build_calls_bootwar(subprocess_mock):
    task = "bootWar"
    command = commands.get(task)
    literal_before = literals.get("gradle_spring_boot_build_before").format(task=task)
    literal_after = literals.get("gradle_spring_boot_build_after").format(task=task)
    literal_error = literals.get("gradle_spring_boot_build_err").format(task=task)

    sut.build("war")

    subprocess_mock.assert_called_once_with(
        command,
        log_before_out=[literal_before],
        log_after_out=[literal_after],
        log_after_err=[literal_error]
    )
