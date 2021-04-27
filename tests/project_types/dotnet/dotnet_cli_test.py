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
    debug = dotnetclidata.debug_argument
    force = "--force"
    expected_command = commands.get("dotnet_restore").format(
        force=force,
        path=path,
        debug=debug)

    # Act
    sut.restore(path, force=True, debug=True)

    # Assert
    call_subprocess_mock.assert_called_once_with(expected_command, log_before_process=[ANY], log_after_err=[ANY])


# endregion restore()

# region build()


@patch("tools.cli.call_subprocess")
def test_restore_given_arguments_then_call_subprocess_with_dotnet_build_command(call_subprocess_mock, dotnetclidata):
    """ Given arguments, should call dotnet build command with arguments converted """
    # Arrange
    path = dotnetclidata.file_path
    debug = dotnetclidata.debug_argument
    force = dotnetclidata.force_argument
    output = dotnetclidata.output_argument
    runtime = dotnetclidata.runtime_argument
    with_restore = dotnetclidata.with_restore_argument
    framework = dotnetclidata.framework_argument
    configuration = dotnetclidata.configuration_argument

    expected_command = commands.get("dotnet_build").format(
        force=force,
        path=path,
        debug=debug,
        output=output,
        runtime=runtime,
        with_restore=with_restore,
        framework=framework,
        configuration=configuration
    )

    # Act
    sut.build(path, configuration=configuration, output=output, framework=framework, runtime=runtime,
              with_restore=False, force=True, debug=True)

    # Assert
    call_subprocess_mock.assert_called_once_with(expected_command, log_before_process=[ANY], log_after_err=[ANY])


# endregion build()

# region publish()


@patch("tools.cli.call_subprocess")
def test_restore_given_arguments_then_call_subprocess_with_dotnet_publish_command(call_subprocess_mock, dotnetclidata):
    """ Given arguments, should call dotnet publish command with arguments converted """
    # Arrange
    path = dotnetclidata.file_path
    self_contained = dotnetclidata.self_contained_argument
    debug = dotnetclidata.debug_argument
    force = dotnetclidata.force_argument
    output = dotnetclidata.output_argument
    runtime = dotnetclidata.runtime_argument
    with_restore = dotnetclidata.with_restore_argument
    framework = dotnetclidata.framework_argument
    configuration = dotnetclidata.configuration_argument

    expected_command = commands.get("dotnet_publish").format(
        force=force,
        path=path,
        debug=debug,
        output=output,
        runtime=runtime,
        with_restore=with_restore,
        framework=framework,
        self_contained=self_contained,
        configuration=configuration
    )

    # Act
    sut.publish(path, configuration=configuration, output=output, framework=framework, runtime=runtime,
                self_contained=False, with_restore=False, force=True, debug=True)

    # Assert
    call_subprocess_mock.assert_called_once_with(expected_command, log_before_process=[ANY], log_after_err=[ANY])

# endregion publish()
