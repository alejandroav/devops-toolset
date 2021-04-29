""" Unit-core for the dotnet/dotnet_cli.py module"""

from unittest.mock import patch, ANY

import project_types.dotnet.dotnet_cli as sut
from core.CommandsCore import CommandsCore
from core.LiteralsCore import LiteralsCore
from project_types.dotnet.commands import Commands as DotnetCommands
from project_types.dotnet.Literals import Literals as DotnetLiterals
from core.app import App

app: App = App()
literals = LiteralsCore([DotnetLiterals])
commands = CommandsCore([DotnetCommands])


# region restore()

@patch("tools.cli.call_subprocess")
def test_restore_given_arguments_then_call_subprocess_with_dotnet_restore_command(call_subprocess_mock, dotnetclidata):
    """ Given arguments, should call dotnet restore command with arguments converted """
    # Arrange
    path = dotnetclidata.file_path
    args = dotnetclidata.converted_args
    expected_command = commands.get("dotnet_restore").format(
        path=path,
        args=args)

    # Act
    sut.restore(path, force=True, output=dotnetclidata.output_argument)

    # Assert
    call_subprocess_mock.assert_called_once_with(expected_command, log_before_process=[ANY], log_after_err=[ANY])


# endregion restore()

# region build()


@patch("tools.cli.call_subprocess")
def test_restore_given_arguments_then_call_subprocess_with_dotnet_build_command(call_subprocess_mock, dotnetclidata):
    """ Given arguments, should call dotnet build command with arguments converted """
    # Arrange
    path = dotnetclidata.file_path
    args = dotnetclidata.converted_args

    expected_command = commands.get("dotnet_build").format(
        path=path,
        args=args
    )

    # Act
    sut.build(path, force=True, output=dotnetclidata.output_argument)

    # Assert
    call_subprocess_mock.assert_called_once_with(expected_command, log_before_process=[ANY], log_after_err=[ANY])


# endregion build()

# region publish()


@patch("tools.cli.call_subprocess")
def test_restore_given_arguments_then_call_subprocess_with_dotnet_publish_command(call_subprocess_mock, dotnetclidata):
    """ Given arguments, should call dotnet publish command with arguments converted """
    # Arrange
    path = dotnetclidata.file_path
    args = dotnetclidata.converted_args

    expected_command = commands.get("dotnet_publish").format(
        args=args,
        path=path
    )

    # Act
    sut.publish(path, force=True, output=dotnetclidata.output_argument)

    # Assert
    call_subprocess_mock.assert_called_once_with(expected_command, log_before_process=[ANY], log_after_err=[ANY])

# endregion publish()
